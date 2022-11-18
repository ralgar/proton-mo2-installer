import sqlite3

class Database:

    def __init__(self):

        self.con = sqlite3.connect('pmf.db')
        self.cursor = self.con.cursor()
        self.create_table('Instances', [
            'ID integer PRIMARY KEY',
            'Platform text',
            'AppID integer',
        ])
        self.create_table('TrackedFiles', [
            'ID integer PRIMARY KEY',
            'InstanceID integer',
            'FilePath text'
        ])

    def __del__(self):
        self.con.close()

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
        self.cursor.execute(data)
        self.con.commit()

    def instance_exists(self, platform_name, app_id):
        query = 'SELECT Platform, AppID from Instances'
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        for row in data:
            if (platform_name == row[0]) and (app_id == row[1]):
                return True

        return False
