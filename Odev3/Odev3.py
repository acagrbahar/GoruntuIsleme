import cv2
import numpy as np
#Alaattin Çağrı Bahar 02215076053

# Görüntüyü oku
image = cv2.imread('C:/Users/alaat/OneDrive/Belgeler/pirinc2.png')

# Gri seviyeye dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gürültüyü azaltmak için GaussianBlur uygula
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Pirinçleri belirlemek için eşikleme uygula
_, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

# istenmeyen alanları temizleme
kernel = np.ones((5, 5), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Etiketleme ve nesne sayısını bulma
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(morph)

# 0. indeks, arka plan olduğu için çıkartılır
num_pirinc = num_labels - 1

# Sonuçları ekrana yazdır
print(f'Toplam {num_pirinc} pirinç tanesi bulundu.')

# Görüntüleri kaydet
cv2.imwrite('C:/Users/alaat/OneDrive/Belgeler/thresh_image.jpg', thresh)
cv2.imwrite('C:/Users/alaat/OneDrive/Belgeler/morph_image.jpg', morph)