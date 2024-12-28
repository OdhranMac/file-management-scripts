"""
This script deletes a series of files defined in an excel spreadsheet.
The excel filename requires the list of filenames under a column heading of 'Filename'.
"""

import pandas as pd
import os

dir = r''

filesToDelete = pd.read_excel(r'', dtype = {'Filename': str})

count = 0

for index, row in filesToDelete.iterrows():
    for dirPaths, subDirs, files in os.walk(dir):
        for currentFile in files:
            if currentFile == row['Filename']:
                print("Deleting: " + currentFile)
                os.remove(os.path.join(dir, currentFile))
                count += 1
        
print("\n" + str(count) + " files deleted")