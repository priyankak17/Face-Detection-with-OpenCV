import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  #loading haarcascade xml
img = cv2.imread('g.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting image to grayscale image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5) #detect multiscale in gray_image, 
#scale factor is imagesize downscaled by 50%

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y),(x+w,y+h), (0, 255, 0), 3) #detect the face and draw a rectangle around it

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

print(type(faces))
print(faces)

cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()