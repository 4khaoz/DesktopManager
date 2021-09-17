import os, sys

class Manager:

    def __init__(self):
        # Get Path of Desktop
        self.desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        

    def sortFilesInDirectory(self, filetype: str):
        file_extension = "." + filetype.lower()
        path = os.path.join(self.desktop, filetype)

        if not os.path.isdir(path):
            # Create Directory if necessary
            os.mkdir(path)

        for file in os.listdir(self.desktop):
            if file.lower().endswith(file_extension):
                os.rename(os.path.join(self.desktop, file), os.path.join(path, file))