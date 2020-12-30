import os
directory = r'C:\Users\Old_02\Desktop\File Renamer Sandbox'
for file in os.scandir(directory):
    print(file.path)
    os.rename(file.path, 'test')