"""
This script allows you to rename a directory of files using an excel table containing both the original filenames and desired filenames.
Enter the directory below, accompanies by an excel file containing headers 'Input Filename' and Output Filename' and execute.
"""

import pandas as pd
import os

dir = r''

filenameTable = pd.read_excel(r'', dtype = {'Input Filename': str, 'Output Filename': str})   

for index, row in filenameTable.iterrows(): 
    input_name = str(row["Input Filename"])
    output_name = str(row["Output Filename"])

    input_name = dir + "\\" + input_name
    output_name = dir + "\\" + output_name

    os.rename(input_name, output_name)
