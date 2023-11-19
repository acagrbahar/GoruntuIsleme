import cv2
import numpy as np

def main():
    # Kamera başlatma
    cam = cv2.VideoCapture(0)

    while True:
        # Görüntüyü yakala
        ret, frame = cam.read()

        # RGB'den HSV'ye dönüştür
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Kırmızı renk aralığı
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])

        # Renk aralığını maskeleyin
        mask = cv2.inRange(hsv, lower_red, upper_red)

        # Görüntüyü sadece maske ile birleştirin
        result = cv2.bitwise_and(frame, frame, mask=mask)

        # Görüntüyü göster
        cv2.imshow('Gerçek Görüntü', frame)
        cv2.imshow('Sonuc', result)

        # Çıkış için 'q' tuşuna basın
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kamera kapatma
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()