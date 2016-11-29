import exifread
import glob
import os
files = glob.glob('*.jpg')
print("Renaming the {} file(s) in this folder with a .jpg ending to a DateTime serial.".format(len(files)))
for f in files:
    f = open(f, 'rb') # Open the file (using exifread)
    tags = exifread.process_file(f) # Get the metadata
    new_name = str(tags['Image DateTime']).replace(':','_')+'.jpg' # Get the DateTime, refomat
    f.close() # close the file (exifread)
    print('Renaming {} to {}'.format(f.name, new_name))
    os.rename(f.name, new_name) # rename (using os)