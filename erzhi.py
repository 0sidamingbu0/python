from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.array(Image.open('img/building.png').convert('L'))

rows, cols = img.shape
for i in range(rows):
    for j in range(cols):
        if img[i, j] <= 130:
            img[i, j] = 0
        else:
            img[i, j] = 1

plt.figure("lena")
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()