"""
This script flattens all the files from subdirectories of 'dirTree' to 'dest' folder.
"""

import shutil
import os

dirTree = os.walk(r'')
dest = r''

for dirPaths, subDirs, files in dirTree:    
    for currentFile in files:
        print(currentFile)
        currentFileFullPath = os.path.join(dirPaths,currentFile)

        if os.path.isfile(currentFileFullPath):
            shutil.copy(currentFileFullPath, dest)