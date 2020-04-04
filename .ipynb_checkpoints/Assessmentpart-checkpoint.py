import cv2
import numpy as np

def draw_circle(event,x,y,flags, params):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 70, (0,0,255), 3)

cv2.namedWindow(winname='my_dog')
cv2.setMouseCallback('my_dog', draw_circle)

img = cv2.imread('data/dog_backpack.jpg')

while True:
    cv2.imshow('my_dog', img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()        
               
               