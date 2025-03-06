import numpy as np
import matplotlib.pyplot as plt
import cv2

#Leer la imagen
img = cv2.imread('imagenFrutas.jpg')
img_color = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#Crear 2 matrices del mismo tamaño
matriz_gray = np.ones(img_gray.shape,dtype='uint8')*50
matriz_RGB = np.ones(img_color.shape,dtype='uint8')*50

#Aumentar el brillo (Suma de imagenes)
brilloRGB = cv2.add(img,matriz_RGB)
brilloRGB = cv2.cvtColor(brilloRGB,cv2.COLOR_BGR2RGB)

#Aumentar el brillo imagen gray
brilloGray = cv2.add(img_gray, matriz_gray)

#Disminuir el brillo (resta de imagenes)
oscuroRGB = cv2.subtract(img,matriz_RGB)
oscuroRGB = cv2.cvtColor(oscuroRGB,cv2.COLOR_BGR2RGB)

#Disminuir el brillo imagen gray
oscuroGray = cv2.subtract(img_gray, matriz_gray)

#Mostrar la imagen
fig = plt.figure()
ax1 = fig.add_subplot(2,3,1)
ax1.imshow(img_color)
ax1.set_title('IMAGEN ORIGINAL')

ax3 = fig.add_subplot(2,3,2)
ax3.imshow(brilloRGB)
ax3.set_title('Brillo con RGB')

ax4 = fig.add_subplot(2,3,3)
ax4.imshow(oscuroRGB)
ax4.set_title('Oscurecer con RGB')

ax2 = fig.add_subplot(2,3,4)
ax2.imshow(img_gray,cmap='gray')
ax2.set_title('IMAGEN GRAY ORIGINAL')

ax5 = fig.add_subplot(2,3,5)
ax5.imshow(brilloGray,cmap='gray')
ax5.set_title('Brillo con Gray')

ax6 = fig.add_subplot(2,3,6)
ax6.imshow(oscuroGray,cmap='gray')
ax6.set_title('Oscurecer con Gray')

plt.show()