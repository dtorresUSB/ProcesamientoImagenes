#Operaciones bit a bit
#(AND, OR, NOT, XOR)

import cv2
import numpy as np
import matplotlib.pyplot as plt

#Crear una imagen negra de 500 x 500
imagen2 = np.zeros((500,500,3), dtype='uint8')
#Crear una  diagonal negra
for i in range(500):
    for j in range(500):
        if i > j:               # Por debajo de la diagonal
            imagen2[i,j] = [140,0,75] # Blanco

#Crear una imagen blancha de 500 x 500
imagen1 = 255 * np.ones((500,500,3), dtype='uint8')
y, x = np.ogrid[:500, :500]     #Crea una matriz de datos para x y y
                                #x => vector fila [1,500]
                                #y => vector columna [500,1]
    
#Crear un circulo de centro 250,250
centro = (250, 250)             
distancia = np.sqrt((x - centro[0])**2 + (y - centro[1])**2)
radio = 200
imagen1[distancia <= radio] = [45,87,44] #crea una matriz de aquellos cuya distancia sea mejor a radio se pintan de cero

#Crear un cuadrado
imagen3 = 255 * np.ones((500, 500, 3), dtype='uint8')
# Definir las coordenadas del rectángulo
x_min, y_min = 100, 70
x_max, y_max = 400, 330

# Crear máscara para el rectángulo
x, y = np.ogrid[:500, :500]
mascara_rectangulo = (x >= x_min) & (x <= x_max) & (y >= y_min) & (y <= y_max)
imagen3[mascara_rectangulo] = [112,84,56]

# Anillo
imagen4 = 255 * np.ones((500, 500, 3), dtype='uint8')

# Definir el centro y radios
centro = (250, 250)
radio_externo = 200
radio_interno = 150

# Crear coordenadas
y, x = np.ogrid[:500, :500]
distancia = np.sqrt((x - centro[0])**2 + (y - centro[1])**2)
mascara_anillo = (distancia <= radio_externo) & (distancia >= radio_interno)

# Aplicar la máscara
imagen4[mascara_anillo] = [239,184,16]


fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(imagen1, cmap='gray')
ax1.set_title('Mascara Circulo')

ax2 = fig.add_subplot(2,2,2)
ax2.imshow(imagen2)
ax2.set_title('Mascara diagonal')

ax3 = fig.add_subplot(2,2,3)
ax3.imshow(imagen3)
ax3.set_title('Mascara cuadrado')

ax4 = fig.add_subplot(2,2,4)
ax4.imshow(imagen4)
ax4.set_title('Anillo')

plt.tight_layout()
plt.show()

#-----------------------Operaciones lógicas------------------
imagen_and = cv2.bitwise_and(imagen1,imagen2,mask=None)

imagen_or = cv2.bitwise_or(imagen1,imagen3,mask=None)

imagen_xor = cv2.bitwise_xor(imagen2,imagen3,mask=None)

imagen_not = cv2.bitwise_not(imagen4,mask=None)

fig = plt.figure(figsize=[12,6])
ax1 = fig.add_subplot(2,4,1)
ax1.imshow(imagen1)
ax1.set_title('Circulo Original')

ax2 = fig.add_subplot(2,4,2)
ax2.imshow(imagen2)
ax2.set_title('Diagonal Original')

ax3 = fig.add_subplot(2,4,3)
ax3.imshow(imagen3)
ax3.set_title('Cuadrado Original')

ax4 = fig.add_subplot(2,4,4)
ax4.imshow(imagen4)
ax4.set_title('Anillo Original')

ax5 = fig.add_subplot(2,4,5)
ax5.imshow(imagen_xor)
ax5.set_title('Imagen XOR (2,3)')

ax5 = fig.add_subplot(2,4,6)
ax5.imshow(imagen_and)
ax5.set_title('Imagen AND (1,2)')

ax6 = fig.add_subplot(2,4,7)
ax6.imshow(imagen_or)
ax6.set_title('Imagen OR (1,4)')

ax7 = fig.add_subplot(2,4,8)
ax7.imshow(imagen_not)
ax7.set_title('Imagen NOT (4)')

plt.tight_layout()
plt.show()

#-----------Operaciones logicas B/N--------------
gray1 = cv2.cvtColor(imagen1,cv2.COLOR_RGB2GRAY)
gray2 = cv2.cvtColor(imagen2,cv2.COLOR_RGB2GRAY)
gray3 = cv2.cvtColor(imagen3,cv2.COLOR_RGB2GRAY)
gray4 = cv2.cvtColor(imagen4,cv2.COLOR_RGB2GRAY)

imagen_and = cv2.bitwise_and(gray1,gray2,mask=None)

imagen_or = cv2.bitwise_or(gray1,gray3,mask=None)

imagen_xor = cv2.bitwise_xor(gray2,gray3,mask=None)

imagen_not = cv2.bitwise_not(gray4,mask=None)

fig = plt.figure(figsize=[12,6])
ax1 = fig.add_subplot(2,4,1)
ax1.imshow(gray1,cmap='gray')
ax1.set_title('Circulo Original')

ax2 = fig.add_subplot(2,4,2)
ax2.imshow(gray2,cmap='gray')
ax2.set_title('Diagonal Original')

ax3 = fig.add_subplot(2,4,3)
ax3.imshow(gray3,cmap='gray')
ax3.set_title('Cuadrado Original')

ax4 = fig.add_subplot(2,4,4)
ax4.imshow(gray4,cmap='gray')
ax4.set_title('Anillo Original')

ax5 = fig.add_subplot(2,4,5)
ax5.imshow(imagen_xor,cmap='gray')
ax5.set_title('Imagen XOR (2,3)')

ax5 = fig.add_subplot(2,4,6)
ax5.imshow(imagen_and,cmap='gray')
ax5.set_title('Imagen AND (1,2)')

ax6 = fig.add_subplot(2,4,7)
ax6.imshow(imagen_or,cmap='gray')
ax6.set_title('Imagen OR (1,4)')

ax7 = fig.add_subplot(2,4,8)
ax7.imshow(imagen_not,cmap='gray')
ax7.set_title('Imagen NOT (4)')

plt.tight_layout()
plt.show()
