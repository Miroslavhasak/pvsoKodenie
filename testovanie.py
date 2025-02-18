import cv2
import os
import numpy as np

#folder
outputFolder = "photo"
mosaicFolder = "mozaika"

count = 0
images = []

mosaic = np.vstack([np.hstack([images[0], images[1]]), np.hstack([images[2], images[3]])])
mosaic_path = os.path.join(mosaicFolder, "mozaika.jpg")

cv2.imwrite(mosaic_path, mosaic)
print(f'Mozaika uložená ako {mosaic_path}')

print('Done.')