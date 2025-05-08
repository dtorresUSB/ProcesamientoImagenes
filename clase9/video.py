import cv2
import numpy as np

parametros = {'maxCorners':50,     #Maximo numero de esquinas a detectar
              'qualityLevel':0.01,   #Umbral mínimo de detección
              'minDistance':10,     #Mínima distancia entre pixeles
              'blockSize':9,        #Area de pixeles
              'mask':None}          #Tipo de mascara

cap = cv2.VideoCapture(1)
print('Seleccione una de las siguientes opciones \n'
      '1. Captura normal de video\n'      #tecla 1
      '2. Captura en grayScale\n'         #tecla 2
      '3. Captura de video HSV\n'         #tecla 3
      )        
opc=49

while True:     #while 1

    status_v,frame =cap.read()

    if opc == 49:
        imagen=frame
    elif opc ==50:
        imagen=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif opc == 51:
        imagen = cv2.applyColorMap(frame,cv2.COLORMAP_PINK)
    elif opc == 52:
        imagen = cv2.blur(frame,(6,6))
    elif opc == 53:
        imagen = cv2.Canny(frame,120,160)
    elif opc == 54:
        imagen = frame
        frameGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        esquinas = cv2.goodFeaturesToTrack(frameGray, **parametros)
        if esquinas is not None:
            for x,y in np.float32(esquinas).reshape(-1,2):
                x,y = int(x), int(y)
                cv2.circle(frame,(x,y), 3, (0,0,255),1)
        


    cv2.imshow('Video',imagen)
    tecla = cv2.waitKey(10)

    if tecla==32:
        print('Salida exitosa')
        break
    elif tecla != -1:
        opc = tecla

cap.release()
cv2.destroyAllWindows()