import cv2
import os
import numpy as np

# Priečinky
mosaicFolder = "mozaika"
mosaic_path = os.path.join(mosaicFolder, "mozaika1.jpg")

# Načítanie existujúcej mozaiky
mosaic = cv2.imread(mosaic_path)

if mosaic is None:
    print(f"Chyba: Súbor {mosaic_path} neexistuje!")
    exit(1)

# Kernel maska (napríklad pre rozostrenie)
kernel = np.array([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]])

# Aplikácia kernel masky na prvý obrázok (ľavý horný)
first_image = mosaic[0:500, 0:500]  # Predpokladáme, že obrázok má veľkosť 600x400
first_image_filtered = cv2.filter2D(first_image, -1, kernel)

# Nahradenie prvého obrázka vo mozaike filtrovaným obrázkom
mosaic[0:500, 0:500] = first_image_filtered

# Uloženie mozaiky
cv2.imwrite(mosaic_path, mosaic)
#print(f"Mozaika uložená ako {mosaic_path}")

# Zobrazenie mozaiky
cv2.imshow("Mozaika s aplikovanym kernelom", mosaic)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Done.")

# mozaika s kernelom