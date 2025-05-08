import cv2
import matplotlib.pyplot as plt
from matplotlib.backend_bases import key_press_handler
import sys

cap = cv2.VideoCapture(0)

def press(event):
   if event.key == 'q':
       plt.close('all')
       sys.exit(0)

fig = plt.figure()
fig.canvas.mpl_connect('key_press_event', press)

while True:
   ret, frame = cap.read()
   if not ret:
       break
       
   frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
   plt.clf()
   plt.imshow(frame_RGB)
   plt.axis('off')
   plt.pause(0.01)
   
cap.release()
plt.close('all')