import cv2
import time
#reading the vriables
countRec = 0

greenLight = cv2.imread("green.jpg")
g = 5
greenTimer = g

yellowLight = cv2.imread("yellow.jpg")
y = 10
yellowTimer = y

redLight = cv2.imread("red.jpg")
r = 15
redTimer = r
#reading the image or video source
img = cv2.imread('car1.jpg') 
#reading the haarcascade classifier
car_cascade = cv2.CascadeClassifier('cars.xml')
#converting the images to gray scale
carImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#applying the haarcascade to detect cars
cars = car_cascade.detectMultiScale(carImg, 1.1, 1)
#for-loop to count all the cars
for (x,y,w,h) in cars:
    #drawing a rectangle over each car
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #number of cars increases by one for every car we find
    countRec = countRec + 1
    #show the cars + the red traffic light
    cv2.imshow("1",img) 
    cv2.imshow("2",redLight)
    
    #start counting when a user clicks any button
    cv2.waitKey(0) 

print("number of cars : ", countRec)
#if-statement to know which traffic light should be one, and run a timer based on that
if countRec > 0 and countRec <= g:
    while greenTimer > 0:
        time.sleep(1)
        print(greenTimer)
        greenTimer -=1


elif countRec > g and countRec <= y and countRec < r:
    while yellowTimer > 0:
        time.sleep(1)
        print(yellowTimer)
        yellowTimer -=1

else:
    while redTimer > 0:
        time.sleep(1)
        print(redTimer)
        redTimer -=1

#show the green-traffic-light when the loop is finished counting
    cv2.imshow("2",greenLight)
#close the program when a user clicks any button
    cv2.waitKey(0)
    cv2.destroyAllWindows()


