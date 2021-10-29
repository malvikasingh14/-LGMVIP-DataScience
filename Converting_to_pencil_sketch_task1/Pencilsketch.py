import cv2
imgloc='C:/Users/91981/Documents/others/WIE/Converting_to_pencil_sketch_task1/picture.jpg' #image location

img= cv2.imread(imgloc) #step1
gryimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #step2
invtgrayimg=255-gryimg #step 3 inverting the image
blurimg=cv2.GaussianBlur(invtgrayimg,(21,21),0) #step 4 bluring 
invtblurimg=255-blurimg #step 5 inverting the blurred image
pencile=cv2.divide(gryimg,invtgrayimg,scale=256.0) #step 6 converting it to pencil sketch

#printing the images...
cv2.imshow('original Image',img)
cv2.imshow('Gray Image',gryimg)
cv2.imshow('Inverted Gray Image',invtgrayimg)
cv2.imshow('Blurr Image',blurimg)
cv2.imshow('Inverted Blurr Image',invtblurimg)
cv2.imshow('Pencil Sketch Image',pencile)
cv2.waitKey(0)
#hence the first task completed.
#thank you!



