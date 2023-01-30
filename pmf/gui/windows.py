import tkinter as tk

import pmf.gui.pages as page

class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.title("Modding Setup Framework")
        # self.attributes('-type', 'dialog')
        self.geometry('800x600')

        self.shared_data = {
            'game':     None,
            'platform': None,
            'task':     None
        }

        # Create the frame container and position it in the root window
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True, padx=10, pady=10)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Using a method to switch frames
        self.show_frame(page.Main)

    def show_frame(self, frame):
        f = frame(self.container, self)
        f.grid(row=0, column=0, sticky="nsew")
        f.tkraise()
