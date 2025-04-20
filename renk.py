import cv2

img = cv2.imread('indir.jpg')

if img is None:
    print("Hata: Görüntü dosyası bulunamadı!")
    exit()

# Orijinal görüntüyü göster
cv2.imshow("Orijinal Goruntu", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 1. Gri tonlamaya çevirme
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_logo.jpg", gray)  # Dosya olarak kaydet
cv2.imshow("Gri Tonlama", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. HSV tonlamaya çevirme
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Tonlama", hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. R (Red) ve B (Blue) kanallarını yer değiştirme
B, G, R = cv2.split(img)
swapped = cv2.merge([R, G, B])  # R ile B yer değiştirdi
cv2.imshow("R ve B Kanallari Degisti", swapped)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. Görselin altına adını siyah renkle yazdırma
cv2.putText(img, "Serhat Alperen Kus", (210, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.imshow("Isimli Gorsel", img)
cv2.waitKey(0)
cv2.destroyAllWindows()