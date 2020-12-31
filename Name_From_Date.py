import os, time
import exifread
directory = r'C:\Users\Old_02\Desktop\File Renamer Test Files'
for file in os.scandir(directory):
    if file.path.lower().endswith(('.tiff', 'jpg', 'jpeg' 'webp', 'heic')):
        print(
            str(file.path)
            #+ ' '
            #+ str(os.path.dirname(file.path))
            #+ '\\' + str(exifread.process_file(open(file.path, 'rb'), details = False)['Image DateTime']).replace(':', '-')
            #+ ' + '
            #+ str(os.path.split(file.path)[-1])
            )
        os.rename(
            file.path,
            str(os.path.dirname(file.path))
            + '\\' + str(exifread.process_file(open(file.path, 'rb'), details = False)['Image DateTime']).replace(':', '-')
            + ' + '
            + str(os.path.split(file.path)[-1])
            )