import cv2
import numpy as np
import matplotlib.pyplot as plt

logo = cv2.imread('oso.png')
fondo = cv2.imread('fondo.png')

logoRGB = cv2.cvtColor(logo,cv2.COLOR_BGR2RGB)
fondoRGB = cv2.cvtColor(fondo,cv2.COLOR_BGR2RGB)

mascara = cv2.cvtColor(logo,cv2.COLOR_RGB2GRAY)
_,imgmask = cv2.threshold(mascara, 50,255,cv2.THRESH_BINARY)

#mascara Invertida
imgmask2 = cv2.bitwise_not(imgmask)
print(logoRGB.shape)
print(fondoRGB.shape)

#operaciones
imagen1 = cv2.bitwise_and(logoRGB,fondoRGB,mask = imgmask)

imagen2 = cv2.bitwise_and(logoRGB,logoRGB, mask = imgmask2)

imagen3 = cv2.add(imagen1,imagen2)

fig = plt.figure()
ax1 = fig.add_subplot(2,3,1)
ax1.imshow(logoRGB)
ax1.set_title('logoRGB')

ax2 = fig.add_subplot(2,3,4)
ax2.imshow(fondoRGB)
ax2.set_title('fondoRGB')

ax3 = fig.add_subplot(2,3,2)
ax3.imshow(imagen1)
ax3.set_title('Imagen 1')

ax4 = fig.add_subplot(2,3,3)
ax4.imshow(imagen2)
ax4.set_title('Imagen 2')

ax5 = fig.add_subplot(2,3,5)
ax5.imshow(imagen3)
ax5.set_title('Imagen final')

ax6 = fig.add_subplot(2,3,6)
ax6.imshow(imgmask, cmap= 'gray')
ax6.set_title('Threshold')

plt.show()
