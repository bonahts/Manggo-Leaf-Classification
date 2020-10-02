import cv2
import matplotlib.pyplot as plt
image = cv2.imread(r'C:\Users\bona\.spyder-py3\manggo2.jpg')
#konversi rgb to grayscale
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
cv2.imwrite("gray.jpg", gray)
cv2.imshow('color_image',image)
cv2.imshow('grayimage',gray) 

plt.imshow(image)
plt.show
cv2.waitKey(0)                 
cv2.destroyAllWindows()


