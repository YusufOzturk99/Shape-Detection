import cv2
from cv2 import waitKey

path = "Resources/shapes.jpg" 
img = cv2.imread(path)
imgContour = img.copy()

def getContours(img):
    contours, hiearchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgContour, cnt, -1,(255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            if objCor ==3: objectType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio <1.05: objectType = "Square"
                else: objectType = "Rectangle" 
            elif objCor == 5: objectType ="Pentagon"
            elif objCor ==6: objectType = "Hexagon"
            elif objCor >6: objectType  = "Circle"
            else :objectType = "None"

            cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType, (x+(w//2)-20, y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)


getContours(imgCanny)

cv2.imshow("Canny", imgCanny)
cv2.imshow("Contour", imgContour)
waitKey(0)