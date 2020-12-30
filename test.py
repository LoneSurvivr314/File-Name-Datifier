import os
import exifread
print(str(exifread.process_file(open(r'C:\Users\Old_02\Desktop\File Renamer Test Files\IMG_0001.HEIC', 'rb'), details = False)['Image DateTime']))