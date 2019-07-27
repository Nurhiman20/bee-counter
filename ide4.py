import numpy as np
import time
import imutils
import cv2

avg = None
video = cv2.VideoCapture("people-capture.mp4")
yvalues = list()
motion = list()
count1 = 0
count2 = 0

def find_majority(k):
    myMap = {}
    maximum = ( '', 0 ) # (occurring element, occurrences)
    for n in k:
        if n in myMap: myMap[n] += 1
        else: myMap[n] = 1

        # Keep track of maximum on the go
        if myMap[n] > maximum[1]: maximum = (n,myMap[n])

    return maximum

while 1:
    ret, frame = video.read()
    flag = True
    text=""

    frame = imutils.resize(frame, width=500)
    # frame = imutils.rotate(frame, angle=90)

    # konversi warna BGR ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # definisikan garis pertama
    lineypos = 225
    cv2.line(frame, (0, lineypos), (width, lineypos), (255, 0, 0), 2)

    # definisikan garis kedua
    lineypos2 = 400
    cv2.line(frame, (0, lineypos3), (width, lineypos2), (0, 255, 0), 2)

    # definiskan range warna merah
    l_merah = np.array([129, 57, 47])
    u_merah = np.array([204, 230, 120])

    # menemukan range warna pada citra
    merah = cv2.inRange(hsv, l_merah, u_merah)

    #morphological transformation, dilation
    kernal = np.ones((5, 5), "uint8")

    merah = cv2.dilate(merah, kernal)
    res2 = cv2.bitwise_and(frame, frame, mask = merah)

    # tracking warna merah
    cnts,hierachy = cv2.findContours(merah, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    cv2.accumulateWeighted(gray, avg, 0.5)
    frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
    thresh = cv2.threshold(frameDelta, 5, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:
        if cv2.contourArea(c) < 5000:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        yvalues.append(y)
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        flag = False
	
    no_y = len(yvalues)
    
    if (no_y > 2):
        difference = yvalues[no_y - 1] - yvalues[no_y - 2]
        if(difference > 0):
            motion.append(1)
        else:
            motion.append(0)

    if flag is True:
        if (no_y > 5):
            val, times = find_majority(motion)
            if val == 1 and times >= 15:
                count1 += 1
            else:
                count2 += 1
                
        yvalues = list()
        motion = list()
    
    cv2.line(frame, (260, 0), (260,480), (0,255,0), 2)
    cv2.line(frame, (420, 0), (420,480), (0,255,0), 2)	
    cv2.putText(frame, "In: {}".format(count1), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, "Out: {}".format(count2), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Frame",frame)
    cv2.imshow("Gray",gray)
    cv2.imshow("FrameDelta",frameDelta)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()