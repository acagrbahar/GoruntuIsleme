import cv2
import numpy as np
from matplotlib import pyplot as plt

#import numpy as np

#histogramı döngülerle hesaplayan bir fonksiyon
def calculate_histogram(foto):
    height, width = foto.shape
    histogram = np.zeros(256, dtype=int)

    for i in range(height):
        for j in range(width):
            pixel_value = foto[i, j]
            histogram[pixel_value] += 1

    return histogram


foto = cv2.imread('../../OneDrive/Belgeler/erci1.jpg',0) #fotoyu oku ve gray modda getir.


cv2.imshow('erciyes', foto) #fotoyu ekranda göster.
cv2.waitKey()

#rgb matrisleri
#B = foto[:,:,0]
#G = foto[:,:,1]
#R = foto[:,:,2]

#rgb matrisleri ekranda görünümü
#cv2.imshow("Mavi",B)
#cv2.imshow("Yesil",G)
#cv2.imshow("Kirmizi",R)
#cv2.waitKey()



#gray modda görünüm
#imGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
#plt.imshow(imGray,cmap='gray')
#plt.show()

histogram = calculate_histogram(foto)

#histogram görselleştirme
plt.figure(figsize=(10, 5))
plt.title('Foto Histogram')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(histogram, color='black')
plt.show()






