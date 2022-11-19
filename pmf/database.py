from os import path

import sqlite3

class Database:

    def __init__(self, db_path='pmf.db'):

        seed = False
        if not path.isfile(db_path):
            seed = True

        self.con = sqlite3.connect(db_path)
        self.cursor = self.con.cursor()

        if seed is True:
            self.seed_database()

    def __del__(self):
        self.con.close()

    def instance_id(self, platform_name):
        query = 'SELECT ID, Platform from Instances'
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        for row in data:
            if platform_name == row[1]:
                return row[0]

        return None

    def execute(self, data):
        self.cursor.execute(data)
        self.con.commit()

    def create_table(self, name, columns):
        data = 'CREATE TABLE IF NOT EXISTS ' + name + '('
        data = data + ', '.join(columns) + ')'
        self.execute(data)

    def create_instance(self, platform_name, app_id):
        data = 'INSERT INTO Instances (Platform, AppID) ' + \
               'VALUES ("' + platform_name + '", ' + str(app_id) + ')'
        self.execute(data)

    def instance_exists(self, platform_name, app_id):
        query = 'SELECT Platform, AppID from Instances'
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        for row in data:
            if (platform_name == row[0]) and (app_id == row[1]):
                return True

        return False

    def seed_database(self):

        self.create_table('Instances', [
            'ID integer PRIMARY KEY',
            'Platform text NOT NULL',
            'AppID integer NOT NULL',
        ])
        self.create_table('TrackedFiles', [
            'ID integer PRIMARY KEY',
            'InstanceID integer NOT NULL',
            'FilePath text NOT NULL'
        ])


    def track_file(self, instance_id, file_path):
        query = 'SELECT InstanceID, FilePath from TrackedFiles'
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        unique = True
        for row in data:
            if row[0] == instance_id:
                if row[1] == file_path:
                    unique = False

        if unique is True:
            data = 'INSERT INTO TrackedFiles (InstanceID, FilePath) ' + \
                   'VALUES (' + str(instance_id) + ', "' + file_path + '")'
            self.cursor.execute(data)
            self.con.commit()
