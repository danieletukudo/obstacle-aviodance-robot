import  cv2
width = 1000
hight = 1000
#import image
img  = cv2.imread("C:/Users/Daniel Samuel/Desktop/road.PNG")
#resize imgae
img_resize = cv2.resize(img,(width,hight))
#crop the image
img_copped= img[200:341,270:300]
#resize croped images
image_resize = cv2.resize(img_copped,(img.shape[1],img.shape[0]))

#display the images
cv2.imshow("image", img)
cv2.imshow("cropped image", img_copped)
cv2.imshow("cropped image", image_resize)
cv2.waitKey(0)
