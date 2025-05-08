import cv2

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()

print(f'Ancho: {cap.get(3)}')
print(f'Alto: {cap.get(4)}')

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo capturar el frame")
        break

    video_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    video_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('Video HSV', video_hsv)
    cv2.imshow('Video GrayScale',video_gray)
    cv2.imshow('video RGB',frame)

    if cv2.waitKey(10) == 32:  # Espacio para salir
        break

cap.release()
cv2.destroyAllWindows()
