#Version usada de OpenCV: 4.1.0
import cv2

img1 = cv2.imread('img-originals/Foto1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('img-originals/Foto1.jpg', cv2.IMREAD_GRAYSCALE)

#Guardar la imagen B/N en formato JPG
cv2.imwrite('img-white-black/Foto-bn.jpg', img2)

# mostrar ambas imagenes en ventanas separadas
cv2.imshow('Imagen original', img1)
cv2.imshow('Imagen en B/N', img2)

cv2.waitKey(0)