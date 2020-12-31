import os
import exifread
#print(str(exifread.process_file(open(r'C:\Users\Old_02\Desktop\File Renamer Test Files\IMG_0037.PNG', 'rb'), details = False)['Image DateTime']))
str(exifread.process_file(open(r'C:\Users\Old_02\Desktop\File Renamer Test Files\IMG_0176.JPG'
, 'rb'), details = False)['Image DateTime'])