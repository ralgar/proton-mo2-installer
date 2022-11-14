'''
This module provides an object for Skyrim LE.
'''

class SkyrimLE:

    def __init__(self):

        self.app_id       = 72850
        self.executable   = "SkyrimLauncher.exe"
        self.name         = "Skyrim LE"
        self.nexus_id     = "skyrim"
        self.protontricks = [ "d3dcompiler_43", "d3dx9" ]
        self.subdirectory = "Skyrim"


    def __str__(self):

        describe = {
            "app_id":       self.app_id,
            "executable":   self.executable,
            "name":         self.name,
            "nexus_id":     self.nexus_id,
            "protontricks": self.protontricks,
            "subdirectory": self.subdirectory,
        }

        return str(describe)
