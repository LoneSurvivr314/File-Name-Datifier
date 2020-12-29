import os, time
import exifread
directory = r'C:\Users\Old_02\Desktop\File Renamer Test Files'
for file in os.scandir(directory):
    print(exifread.process_file(open(file.path, 'rb')))
    