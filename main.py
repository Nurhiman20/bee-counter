import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

fps, width, height = cap.get(cv2.CAP_PROP_FPS), cap.get(
    cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = int(width)
height = int(height)
print(fps, width, height)

while True:
    # mengambil citra
    _, frame = cap.read()

    # konversi warna BGR ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # range warna yang harus dideteksi (dalam mode warna HSV)
    l_b = np.array([34, 50, 30])
    u_b = np.array([89, 255, 95])
    mask = cv2.inRange(hsv, l_b, u_b)
    
    # gambar kontur
    contours,hierachy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    
    # area pertama
    lineypos = 225
    cv2.line(frame, (0, lineypos), (width, lineypos), (255, 0, 0), 2)
    lineypos2 = 235
    cv2.line(frame, (0, lineypos2), (width, lineypos2), (255, 0, 0), 2)
    
    # area kedua
    lineypos3 = 400
    cv2.line(frame, (0, lineypos3), (width, lineypos3), (0, 255, 0), 2)
    lineypos4 = 410
    cv2.line(frame, (0, lineypos4), (width, lineypos4), (0, 255, 0), 2)
    
    # batas ukuran tagging yang terbaca
    minarea = 10
    maxarea = 50000
    
    cxx = np.zeros(len(contours))
    cyy = np.zeros(len(contours))

    for i in range(len(contours)):  # cycles through all contours in current frame

        if hierachy[0, i, 3] == -1:  # using hierarchy to only count parent contours (contours not within others)

            area = cv2.contourArea(contours[i])  # area of contour

            if minarea < area < maxarea:  # area threshold for contour

                # calculating centroids of contours
                cnt = contours[i]
                M = cv2.moments(cnt)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                if lineypos < cy < lineypos2:   # kirim data saat melewati area pertama
                    print(area)

                elif cy > lineypos:  # filters out contours that are above line (y starts at top)

                    # gets bounding points of contour to create rectangle
                    # x,y is top left corner and w,h is width and height
                    x, y, w, h = cv2.boundingRect(cnt)

                    # creates a rectangle around contour
                    cv2.rectangle(frame, (x, y), (x + w, y + h), cv2.mean(frame, mask), 2)
    
    
    kernel = np.ones((15,15), np.float32)/255
    
    # dilation = cv2.dilate(frame, kernel, iterations = 1)
    opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)

    # res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    # cv2.imshow("mask", mask)
    # cv2.imshow("dilation", dilation)
    # cv2.imshow("opening", opening)
    # cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()