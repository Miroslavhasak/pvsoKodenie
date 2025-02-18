from ximea import xiapi
import cv2
import os
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

while 0 < count:
  key = cv2.waitKey()
    if key == ord('q')
      break
  cam.get_image(img)
  data = img.get_image_data_numpy()
  file_path = os.path.join(outputFolder, f'snimka{count + 1}.jpg')
  cv2.imwrite(file_path, data)
  print(f'Snímka uložená ako {file_path}')
  image = img.get_image_data_numpy()
  image = cv2.resize(image,(1500,900))
  cv2.imshow("test", image)
  count += 1
  cv2.waitKey()

#stop data acquisition
print('Stopping acquisition...')
cam.stop_acquisition()

#stop communication
cam.close_device()

print('Done.')
