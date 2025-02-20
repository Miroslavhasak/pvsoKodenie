from ximea import xiapi
import cv2
import os
import numpy as np
### runn this command first echo 0|sudo tee /sys/module/usbcore/parameters/usbfs_memory_mb  ###

#create instance for first connected camera
cam = xiapi.Camera()

#start communication
#to open specific device, use:
#cam.open_device_by_SN('41305651')
#(open by serial number)
print('Opening first camera...')
cam.open_device()

#folder
outputFolder = "photo"
mosaicFolder = "mozaika"

#settings
cam.set_exposure(100000)
cam.set_param('imgdataformat','XI_RGB32')
cam.set_param('auto_wb', 1)
print('Exposure was set to %i us' %cam.get_exposure())

#create instance of Image to store image data and metadata
img = xiapi.Image()

#start data acquisition
print('Starting data acquisition...')
cam.start_acquisition()

"""
while cv2.waitKey() != ord('q'):
  while
  cam.get_image(img)
  data = img.get_image_data_numpy()
  # Uložíme obrázok pomocou OpenCV
  file_path = os.path.join(outputFolder, f'snimka{count + 1}.jpg')
  cv2.imwrite(file_path, data)
  print(f'Snímka uložená ako {file_path}')

  image = img.get_image_data_numpy()
  image = cv2.resize(image,(1500,900))
  cv2.imshow("test", image)
  count += 1
  cv2.waitKey()
"""

count = 0
# uloha 1
while 0 < count:
  key = cv2.waitKey()
    if key == ord('q')
      break
  cam.get_image(img)
  data = img.get_image_data_numpy()
  file_path = os.path.join(outputFolder, f'snimka{count + 1}.jpg')
  cv2.imwrite(file_path, data)
  # print(f'Snímka uložená ako {file_path}')
  image = img.get_image_data_numpy()
  image = cv2.resize(image,(1500,900))
  cv2.imshow("test", image)
  count += 1
  cv2.waitKey()

# uloha 2 mozaika
image_filenames = [f"snimka{i+1}.jpg" for i in range(4)]
images = []

for filename in image_filenames:
    path = os.path.join(outputFolder, filename)
    if os.path.exists(path):
        img = cv2.imread(path)
        images.append(cv2.resize(img, (500, 500)))  
    else:
        print(f"Chyba: Súbor {filename} neexistuje!")
        exit(1)

mosaic = np.vstack([np.hstack([images[0], images[1]]), np.hstack([images[2], images[3]])])
mosaic_path = os.path.join(mosaicFolder, "mozaika1.jpg")
cv2.imwrite(mosaic_path, mosaic)   

# uloha 3 kernel na prvy obrazok
if mosaic is None:
    print(f"Chyba: Súbor {mosaic_path} neexistuje!")
    exit(1)

kernel = np.array([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]])

first_image = mosaic[0:500, 0:500] 
first_image_filtered = cv2.filter2D(first_image, -1, kernel)

mosaic[0:500, 0:500] = first_image_filtered

cv2.imwrite(mosaic_path, mosaic)

# uloha 4 otocenie snimky o 90 stupnov
img_height = mosaic.shape[0] // 2  
img_width = mosaic.shape[1] // 2   

second_image = mosaic[0:img_height, img_width:img_width * 2]  
rotated_image = np.zeros((img_height, img_width, 3), dtype=np.uint8) 

for i in range(img_height):
    for j in range(img_width):
        rotated_image[j, img_width - 1 - i] = second_image[i, j]  

mosaic[0:img_height, img_width:img_width * 2] = rotated_image

# Uloženie mozaiky
mosaic_result_path = os.path.join(mosaicFolder, "mozaika_upravena.jpg")
cv2.imwrite(mosaic_result_path, mosaic)

# uloha 5 cerveny treti obrazok
img_height = mosaic.shape[0] // 2  
img_width = mosaic.shape[1] // 2   

third_image = mosaic[img_height:img_height * 2, 0:img_width].copy()

only_red = np.zeros_like(third_image)
only_red[:, :, 2] = third_image[:, :, 2]  

# Nahradenie tretieho obrázka v mozaike upravenou verziou
mosaic[img_height:img_height * 2, 0:img_width] = only_red

# uloha 6 vypisanie informacii o obrazku
mosaic_result_path = os.patprint(f"rozmery: {mosaic.shape[0]} x {mosaic.shape[1]} px")
print(f"pocet kanalov: {mosaic.shape[2]}")
print(f"datovy typ: {mosaic.dtype}")
print(f"velkost v pamati: {mosaic.size * mosaic.itemsize} B ({round(mosaic.size * mosaic.itemsize / 1024, 2)} KB)")

img_height = mosaic.shape[0] // 2  
img_width = mosaic.shape[1] // 2

# zobrazenie mozaiky
cv2.imshow("Mozaika s upravenymi obrazkami", mosaic)
cv2.waitKey(0)
cv2.destroyAllWindows()

#stop data acquisition
print('Stopping acquisition...')
cam.stop_acquisition()

#stop communication
cam.close_device()

print('Done.')