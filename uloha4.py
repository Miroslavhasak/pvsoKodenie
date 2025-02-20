import cv2
import os
import numpy as np

# Priečinok a cesta k mozaike
mosaicFolder = "mozaika"
mosaic_path = os.path.join(mosaicFolder, "mozaika1.jpg")

# Načítanie existujúcej mozaiky
mosaic = cv2.imread(mosaic_path)

if mosaic is None:
    print(f"Chyba: Súbor {mosaic_path} neexistuje!")
    exit(1)

# Predpokladaná veľkosť jednotlivých obrázkov v mozaike
img_height = mosaic.shape[0] // 2  # Polovica výšky mozaiky
img_width = mosaic.shape[1] // 2   # Polovica šírky mozaiky

# Otočenie druhého obrázka (pravý horný) o 90° pomocou `for` cyklu
second_image = mosaic[0:img_height, img_width:img_width * 2]  # Vystrihnutie druhého obrázka
rotated_image = np.zeros((img_height, img_width, 3), dtype=np.uint8)  # Zachovanie správnych rozmerov!

# Transponovanie pixelov manuálne (otočenie o 90° v smere hodinových ručičiek)
for i in range(img_height):
    for j in range(img_width):
        rotated_image[j, img_width - 1 - i] = second_image[i, j]  # Správne otočenie pixelov

# Nahradenie druhého obrázka otočenou verziou
mosaic[0:img_height, img_width:img_width * 2] = rotated_image

# Uloženie mozaiky
mosaic_result_path = os.path.join(mosaicFolder, "mozaika_upravena.jpg")
cv2.imwrite(mosaic_result_path, mosaic)
print(f"Upravená mozaika uložená ako {mosaic_result_path}")

# Zobrazenie mozaiky
cv2.imshow("Mozaika s otocenym druhym obrazkom", mosaic)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Done.")
# otocenie snimky o 90 stupnov