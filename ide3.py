import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fps, width, height = cap.get(cv2.CAP_PROP_FPS), cap.get(
    cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = int(width)
height = int(height)
print(fps, width, height)

while True :
    # mengambil citra
    _, frame = cap.read()

    # konversi warna BGR ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # definisikan area pertama
    lineypos = 225
    cv2.line(frame, (0, lineypos), (width, lineypos), (255, 0, 0), 2)
    lineypos2 = 235
    cv2.line(frame, (0, lineypos2), (width, lineypos2), (255, 0, 0), 2)
    
    # definisikan area kedua
    lineypos3 = 400
    cv2.line(frame, (0, lineypos3), (width, lineypos3), (0, 255, 0), 2)
    lineypos4 = 410
    cv2.line(frame, (0, lineypos4), (width, lineypos4), (0, 255, 0), 2)
    
    # definiskan range warna hijau
    l_hijau = np.array([34, 50, 30])
    u_hijau = np.array([89, 255, 95])

    # definiskan range warna kuning
    l_kuning = np.array([14, 110, 85])
    u_kuning = np.array([55, 255, 139])

    # definiskan range warna merah
    l_merah = np.array([176, 90, 0])
    u_merah = np.array([255, 212, 121])

    # menemukan range warna pada citra
    hijau = cv2.inRange(hsv, l_hijau, u_hijau)
    kuning = cv2.inRange(hsv, l_kuning, u_kuning)
    merah = cv2.inRange(hsv, l_merah, u_merah)

    # morphological transformation, opening
    kernel = np.ones((15,15), np.float32)/255
    
    hijau = cv2.morphologyEx(hijau, cv2.MORPH_OPEN, kernel)
    res = cv2.bitwise_and(frame, frame, mask = hijau)

    kuning = cv2.morphologyEx(kuning, cv2.MORPH_OPEN, kernel)
    res1 = cv2.bitwise_and(frame, frame, mask = kuning)

    merah = cv2.morphologyEx(merah, cv2.MORPH_OPEN, kernel)
    res2 = cv2.bitwise_and(frame, frame, mask = merah)

    # tracking warna hijau
    contours,hierachy = cv2.findContours(hijau, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 10):
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(frame, (x,y), (x+w, y+h), (121,43,236), 2)
    
    cv2.imshow("frame", frame)

    # menutup frame / program
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()