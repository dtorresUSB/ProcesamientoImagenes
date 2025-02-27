import cv2
import matplotlib.pyplot as plt

#--------------------------------Lectura de Imagenes------------------------------------

imagen = cv2.imread('goku.jpg')         #Realiza la correccion de color (de BGR a RGB)
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

#Mostrar la imagen utilizando matplotlib
plt.imshow(imagen_rgb)
plt.show()

#Extraer los valores de las matrices de RGB
R,G,B = cv2.split(imagen_rgb)
print(R.shape, G.shape, B.shape)

#Mostrar la imagen utilizando cv2
cv2.imshow('Primera Imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Crear una nueva figura
fig = plt.figure()
#Capa Roja (subplot posicion 1)
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(R,cmap='gray')
ax1.set_title('Capa Roja')

#Capa Verde (subplot posicion 2)
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(G,cmap='gray')
ax2.set_title('Capa Verde')

#Capa Roja (subplot posicion 3)
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(B,cmap='gray')
ax3.set_title('Capa Azul')

#Imagen Original (subplot posicion 4)
ax3 = fig.add_subplot(2,2,4)
ax3.imshow(imagen_rgb)
ax3.set_title('Imagen original')

print(imagen[1,1,:])        #Imprimir los valores del pixel 1

plt.show()

#---------------------- Imagenes colores HSV ----------------------

# Leer la imagen
imagen = cv2.imread('goku.jpg')
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Crear una figura con subplots
plt.figure(figsize=(12,4))

# Mostrar los canales HSV por separado
h, s, v = cv2.split(imagen_hsv)

# Mostrar imagen RGB
plt.subplot(2,2,1)
plt.imshow(h,cmap='gray')
plt.title('Matiz')
plt.axis('off')

# Mostrar imagen HSV
plt.subplot(2,2,2)
plt.imshow(s,cmap='gray')
plt.title('Saturacion')
plt.axis('off')

plt.subplot(2,2,3)
# # Apilar los canales verticalmente
# canales_hsv = np.vstack((h, s, v))
plt.imshow(v,cmap='gray')
plt.title('Brillo')
plt.axis('off')

plt.subplot(2,2,4)
# # Apilar los canales verticalmente
# canales_hsv = np.vstack((h, s, v))
plt.imshow(imagen_rgb)
plt.title('Original')
plt.axis('off')

plt.tight_layout()
plt.show()

# --------------------- Reconstrucción de una imagen ----------------

imagen = cv2.imread('goku.jpg')
#Realiza la correccion de color (de BGR a RGB)
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
R,G,B = cv2.split(imagen_rgb)
imagen_rgb = cv2.merge(((R+50),G,B))

#guardar la imagen
imagen_bgr=cv2.cvtColor(imagen_rgb, cv2.COLOR_RGB2BGR)
cv2.imwrite('NuevaImagen.PNG',imagen_rgb)
plt.imsave('NuevaImagen2.png',imagen_rgb)

plt.imshow(imagen_rgb)
plt.show()