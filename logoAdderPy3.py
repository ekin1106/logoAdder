import os
import time
from PIL import Image

"""James' Logo adding tool for StartUp Algonquin -
It adds the StartUp Algonquin logo to batches of photos
Version 1.0 for Python 3"""

#Load the image
SQUARE_FIT_SIZE = 300.0
print("This is James' logo adding tool version 1.0 PYTHON 3")
print("\n**************************\n")

LOGO_FILENAME = input("Enter a file name: ")
ratio = eval(input("Enter the ratio of the logo to the image: "))

if not os.path.exists('withLogo'):
    os.makedirs('withLogo')

#Timer start
start = time.clock()
count = 0
#Loop over all photos in a directory
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
	or filename == LOGO_FILENAME:
	    continue

    logoIm = Image.open(LOGO_FILENAME)
    logoWidth, logoHeight = logoIm.size
		
    # change this ratio variable according to the width of the image
    aspRatio = float(logoWidth / logoHeight)

    im = Image.open(filename) 
    imWidth, imHeight = im.size
    logoWidth = int(imWidth * ratio)
    logoHeight = int(logoWidth / aspRatio)
    logoIm = logoIm.resize((logoWidth, logoHeight), Image.ANTIALIAS)

    print('Adding %s to %s...' %(LOGO_FILENAME, filename))
    im.paste(logoIm, (0, 0), logoIm)

    #save the images in a new folder
    im.save(os.path.join('withLogo', filename))
    
    count += 1
	
#Timer end
end = time.clock() - start
print("\n**************************\n")
print("%d files done in %d seconds." %(count, end))
