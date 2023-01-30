import threading
import tkinter as tk
from tkinter import ttk

from pmf import database
from pmf import games
from pmf import platforms

class Main(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        text = '''
===============================================
===   Welcome to Modding Setup Framework!   ===
===============================================

Please read these instructions carefully before continuing.

1. Install your chosen game through your platform (eg. Steam) before continuing.
2. Read these instructions carefully, and follow the prompts until finished.
3. When the installation is complete, launch the game as normal.

Notes:
  - The installer may interact with your chosen platform in various ways. This
    may include closing running instances, or launching the game to initialize
    the prefix. Do NOT interfere with this process, or the installation may fail.
  - Configuring the prefix may take a long time in some cases. Please be patient,
    the process will finish eventually.

Visit https://github.com/ralgar/proton-mo2-installer for more info.
'''
        textbox = tk.Text(self)
        textbox.insert(tk.END, text)
        textbox.config(state='disabled')
        textbox.pack(expand=True, fill=tk.BOTH, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Continue",
            command=lambda: controller.show_frame(SelectPlatform),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class SelectPlatform(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.platform = tk.StringVar()

        label = tk.Label(self, text="Select a Platform:")
        label.pack(padx=10, pady=10)

        choices = tk.Variable(value=platforms.platforms)
        self.listbox = tk.Listbox(
            self,
            listvariable=choices,
            selectmode=tk.SINGLE
        )
        self.listbox.pack(expand=True, fill=tk.BOTH, pady=10)
        self.listbox.bind('<<ListboxSelect>>', self.selection_changed)

        self.button = tk.Button(
            self,
            text="Continue",
            command=threading.Thread(target=self.finalize_selection).start
        )
        self.button.pack(side="bottom", fill=tk.X)

    def selection_changed(self, _):
        for i in self.listbox.curselection():
            self.platform = self.listbox.get(i)

    def finalize_selection(self):
        self.button['state'] = 'disabled'
        shared_data = self.controller.shared_data
        if self.platform == 'Steam':
            shared_data.update({'platform': platforms.steam.Steam()})
        if self.platform == 'Steam Flatpak':
            shared_data.update({'platform': platforms.steam.SteamFlatpak()})

        self.controller.show_frame(SelectGame)


class SelectGame(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.game = tk.StringVar()

        label = tk.Label(self, text="Select a Game:")
        label.pack(padx=10, pady=10)

        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.games = self.find_games()
        for _, name in self.games.items():
            self.listbox.insert(tk.END, name)
        self.listbox.pack(expand=True, fill=tk.BOTH, pady=10)
        self.listbox.bind('<<ListboxSelect>>', self.selection_changed)

        self.switch_window_button = tk.Button(
            self,
            text="Continue",
            command=self.finalize_selection
        )
        self.switch_window_button.pack(side="bottom", fill=tk.X)

    def find_games(self):

        steam_apps = self.controller.shared_data['platform'].list_appids()

        # Make a list of supported AppIDs
        apps = {}
        for appid, name in games.games.items():
            for steam_app in steam_apps:
                if appid == steam_app:
                    apps.update({appid:name})

        return apps

    def selection_changed(self, _):
        for i in self.listbox.curselection():
            for appid, name in games.games.items():
                if name == self.listbox.get(i):
                    self.game = appid

    def finalize_selection(self):
        self.controller.shared_data['game'] = games.init(
            self.controller.shared_data['platform'],
            self.game
        )

        self.controller.show_frame(SelectTask)


class SelectTask(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.task = tk.StringVar()

        label = tk.Label(self, text="Select a Task to perform:")
        label.pack(padx=10, pady=10)

        choices = tk.Variable(value=self.get_choices())
        self.listbox = tk.Listbox(
            self,
            listvariable=choices,
            selectmode=tk.SINGLE
        )
        self.listbox.pack(expand=True, fill=tk.BOTH, pady=10)
        self.listbox.bind('<<ListboxSelect>>', self.selection_changed)

        self.switch_window_button = tk.Button(
            self,
            text="Continue",
            command=self.finalize_selection
        )
        self.switch_window_button.pack(side="bottom", fill=tk.X)

    def get_choices(self):

        db       = database.Database()
        game     = self.controller.shared_data['game']
        platform = self.controller.shared_data['platform']

        if db.instance_exists(platform.name, game.app_id) is False:
            choices = [ 'Install' ]
        else:
            choices = [ 'Upgrade', 'Uninstall' ]

        del db
        return choices

    def selection_changed(self, _):
        for i in self.listbox.curselection():
            self.task = self.listbox.get(i)

    def finalize_selection(self):
        shared_data = self.controller.shared_data
        if self.task in ('Install', 'Upgrade'):
            shared_data.update({'task': self.task})
            self.controller.show_frame(Install)
        if self.task == 'Uninstall':
            self.controller.show_frame(Completion)


class Install(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="Confirm")
        self.label.pack(padx=10, pady=10)

        self.progress = ttk.Progressbar(self, mode='indeterminate', length=400)
        self.progress.pack(anchor=tk.CENTER)

        self.button = tk.Button(
            self,
            text="Begin Installation",
            command=threading.Thread(target=self.install).start
        )
        self.button.pack(side="bottom", fill=tk.X)

    def install(self):
        db       = database.Database()
        game     = self.controller.shared_data['game']
        platform = self.controller.shared_data['platform']
        task     = self.controller.shared_data['task']

        self.button['state']='disabled'
        self.progress.start()
        if task != 'Upgrade':
            db.create_instance(platform.name, game.app_id)
        game.install(self, db)
        del db
        self.progress.stop()
        self.button['state']='normal'
        self.controller.show_frame(Completion)


class Completion(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Installation complete!")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Exit",
            command=controller.destroy
        )
        switch_window_button.pack(side="bottom", fill=tk.X)
