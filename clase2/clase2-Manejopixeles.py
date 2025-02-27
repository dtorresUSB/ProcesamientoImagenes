import numpy as np
import cv2
import matplotlib.pyplot as plt

#-------------------------Manejo de matrices (pixeles grayScale)---------------------------------
#Crear una imagen de 10x10 px completamente negra

imagen = np.zeros((10,10),np.uint8)
print(imagen)

#Modificar pixeles dentro de la imagen
imagen[0,1] =30
imagen[2,3] =50
imagen[4,5] =140
imagen[6,7] =200
imagen[8,9] = 255

# #Mostrar la imagen usando matplotlib
plt.imshow(imagen,cmap='gray')
plt.show()

#Mostrar la imagen usando cv2
imagen_ampliada = cv2.resize(imagen, (200, 200))
cv2.imshow('Primera Imagen',imagen_ampliada)
cv2.waitKey(0)
cv2.destroyAllWindows()
#----------------------------Manejo de matrices (pixeles RGB)-------------------------------------------------

#Crear ahora una matriz de RGB
imagen = 255*np.ones((10,10,3),np.uint8)    #pinta color blanco

#Se modifica el tono de una de las matrices
imagen[:5,5:,0] = 0     # Modificando la capa 0 (capa R)

#Guardando cada una de las capas por aparte
red = imagen[:,:,0]
green = imagen[:,:,1]
blue = imagen[:,:,2]

print(green)

plt.imshow(imagen)
plt.show()
