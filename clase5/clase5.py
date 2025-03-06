#Leer la imagen
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imagenFrutas.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

matriz = np.ones(gray.shape, dtype='uint8')*50


#Umbralizacion básica
#retval, dst = cv2.threshold(imagen, tresh(debajo=0, encima=255),maxValue, tipo de umbral)

#Umbralizacion adaptativa
#dst = cv2.adaptativeThreshold(imagen, maxValue, adaptiveMethod, thresholdType, blocksize)

brilloGray = cv2.add(gray, matriz)

_,imgthresh1 = cv2.threshold(brilloGray, 160, 255, cv2.THRESH_BINARY)
_,imgthresh2 = cv2.threshold(brilloGray, 160, 255, cv2.THRESH_BINARY_INV)

adapt_imgthres1 = cv2.adaptiveThreshold(brilloGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)

oscuroGray = cv2.subtract(gray,matriz)

_,imgthresh3 = cv2.threshold(oscuroGray, 50, 255, cv2.THRESH_BINARY)
_,imgthresh4 = cv2.threshold(oscuroGray, 50, 255, cv2.THRESH_BINARY_INV)

adapt_imgthres2 = cv2.adaptiveThreshold(oscuroGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,11,7)

#Mostrar la imagen
fig = plt.figure()
ax1 = fig.add_subplot(2,4,1)
ax1.imshow(brilloGray,cmap='gray')
ax1.set_title('ImagenGray')

ax3 = fig.add_subplot(2,4,2)
ax3.imshow(imgthresh1,cmap='gray')
ax3.set_title('Brillo Thresh 1')

ax4 = fig.add_subplot(2,4,3)
ax4.imshow(imgthresh2,cmap='gray')
ax4.set_title('Brillo Thresh 2')

ax2 = fig.add_subplot(2,4,4)
ax2.imshow(adapt_imgthres1,cmap='gray')
ax2.set_title('Brillo adap_Thresh 1')

ax5 = fig.add_subplot(2,4,5)
ax5.imshow(oscuroGray,cmap='gray')
ax5.set_title('Oscuro con Gray')

ax6 = fig.add_subplot(2,4,6)
ax6.imshow(imgthresh3,cmap='gray')
ax6.set_title('Oscuro Thresh 3')

ax7 = fig.add_subplot(2,4,7)
ax7.imshow(imgthresh4,cmap='gray')
ax7.set_title('Oscuro Thresh 4')

ax8 = fig.add_subplot(2,4,8)
ax8.imshow(adapt_imgthres2,cmap='gray')
ax8.set_title('Oscuro adap_Thresh 2')

plt.show()