import cv2

img = cv2.imread('baboon.jpg')

while True:
    cv2.imshow('Bab', img)
    
    if cv2.waitKey(1) & 0xFF == 27 :
        break

cv2.destroyAllWindows()