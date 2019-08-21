import numpy as np
import time
import imutils
import cv2
import serial
import MySQLdb as mdb

avg = None
# video = cv2.VideoCapture("people-capture.mp4")
video = cv2.VideoCapture(0)
yvalues_merah = list()
motion_merah = list()
yvalues_biru = list()
motion_biru = list()
yvalues_hijau = list()
motion_hijau = list()
yvalues_kuning = list()
motion_kuning = list()
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0

# menghubungkan dengan database
con = mdb.connect('localhost','pi','linggarestu123','mydb');

fps, width, height = video.get(cv2.CAP_PROP_FPS), video.get(
    cv2.CAP_PROP_FRAME_WIDTH), video.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = int(width)
height = int(height)
print(fps, width, height)

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
    lineypos = 100
    cv2.line(frame, (0, lineypos), (width, lineypos), (255, 0, 0), 2)

    # definisikan garis kedua
    lineypos2 = 300
    cv2.line(frame, (0, lineypos2), (width, lineypos2), (0, 255, 0), 2)

    # definiskan range warna
    l_merah = np.array([0, 73, 58])
    u_merah = np.array([183, 115, 84])
    l_biru = np.array([129, 23, 54])
    u_biru = np.array([162, 39, 75])
    l_hijau = np.array([16, 10, 47])
    u_hijau = np.array([116, 27, 74])
    l_kuning = np.array([22, 71, 65])
    u_kuning = np.array([39, 113, 104])
    
    # menemukan range warna pada citra
    merah = cv2.inRange(hsv, l_merah, u_merah)
    biru = cv2.inRange(hsv, l_biru, u_biru)
    hijau = cv2.inRange(hsv, l_hijau, u_hijau)
    kuning = cv2.inRange(hsv, l_kuning, u_kuning)

    #morphological transformation, dilation
    kernal = np.ones((5, 5), "uint8")

    merah = cv2.dilate(merah, kernal)
    res2 = cv2.bitwise_and(frame, frame, mask = merah)
    
    biru = cv2.dilate(biru, kernal)
    res2 = cv2.bitwise_and(frame, frame, mask = biru)

    hijau = cv2.dilate(hijau, kernal)
    res2 = cv2.bitwise_and(frame, frame, mask = hijau)
    
    kuning = cv2.dilate(kuning, kernal)
    res2 = cv2.bitwise_and(frame, frame, mask = kuning)

    # tracking warna merah
    cnts_merah,hierachy = cv2.findContours(merah, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, cnts_merah, -1, (0, 255, 0), 3)

    for c in cnts_merah:
        if cv2.contourArea(c) < 100:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        yvalues_merah.append(y)
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        flag = False
	
    no_y_merah = len(yvalues_merah)
    
    if (no_y_merah > 2):
        difference_merah = yvalues_merah[no_y_merah - 1] - yvalues_merah[no_y_merah - 2]
        if(difference_merah > 0):
            motion_merah.append(1)
        else:
            motion_merah.append(0)

    if flag is True:
        if (no_y_merah > 5):
            val, times = find_majority(motion_merah)
            if val == 1 and times >= 10:
                count2 += 1
                query2 = "INSERT INTO koloni2 (id, warna_lebah, status, waktu) VALUES (NULL,'merah', 'keluar', now());"
                cursor = con.cursor()
                cursor.execute(query2)
                con.commit()
                print("keluar", yvalues_merah)
                # print(motion_merah)
                # print(val)
                
            elif val == 0 and times >= 10:
                count1 += 1
                query1 = "INSERT INTO koloni2 (id, warna_lebah, status, waktu) VALUES (NULL,'merah', 'masuk', now());"
                cursor = con.cursor()
                cursor.execute(query1)
                con.commit()
                print("masuk", yvalues_merah)
                # print(motion_merah)
                # print(val)

        yvalues_merah = list()
        motion_merah = list()
    
    # tracking warna biru
    cnts_biru,hierachy = cv2.findContours(biru, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, cnts_biru, -1, (0, 255, 0), 3)

    for d in cnts_biru:
        if cv2.contourArea(d) < 100:
            continue
        (x, y, w, h) = cv2.boundingRect(d)
        yvalues_biru.append(y)
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        flag = False
	
    no_y_biru = len(yvalues_biru)
    
    if (no_y_biru > 2):
        difference_biru = yvalues_biru[no_y_biru - 1] - yvalues_biru[no_y_biru - 2]
        if(difference_biru > 0):
            motion_biru.append(1)
        else:
            motion_biru.append(0)

    if flag is True:
        if (no_y_biru > 5):
            val, times = find_majority(motion_biru)
            if val == 1 and times >= 10:
                count4 += 1
                query4 = "INSERT INTO koloni2 (id, warna_lebah, status, waktu) VALUES (NULL,'biru', 'keluar', now());"
                cursor = con.cursor()
                cursor.execute(query4)
                con.commit()
                print("keluar", yvalues_biru)
                # print(motion_biru)
                # print(val)
                
            elif val == 0 and times >= 10:
                count3 += 1
                query3 = "INSERT INTO koloni2 (id, warna_lebah, status, waktu) VALUES (NULL,'biru', 'masuk', now());"
                cursor = con.cursor()
                cursor.execute(query3)
                con.commit()
                print("masuk", yvalues_biru)
                # print(motion_biru)
                # print(val)

        yvalues_biru = list()
        motion_biru = list()

    # tracking warna hijau 
    cnts_hijau,hierachy = cv2.findContours(hijau, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, cnts_hijau, -1, (0, 255, 0), 3)

    for e in cnts_hijau:
        if cv2.contourArea(e) < 100:
            continue
        (x, y, w, h) = cv2.boundingRect(e)
        yvalues_hijau.append(y)
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        flag = False
	
    no_y_hijau = len(yvalues_hijau)
    
    if (no_y_hijau > 2):
        difference_hijau = yvalues_hijau[no_y_hijau - 1] - yvalues_hijau[no_y_hijau - 2]
        if(difference_hijau > 0):
            motion_hijau.append(1)
        else:
            motion_hijau.append(0)

    if flag is True:
        if (no_y_hijau > 5):
            val, times = find_majority(motion_hijau)
            if val == 1 and times >= 10:
                count6 += 1
                query6 = "INSERT INTO koloni2 (id, warna_lebah, status, waktu) VALUES (NULL,'hijau', 'keluar', now());"
                cursor = con.cursor()
                cursor.execute(query6)
                con.commit()
                print("keluar", yvalues_hijau)
                # print(motion_hijau)
                print(val)
                
            elif val == 0 and times >= 10:
                count5 += 1
                query5 = "INSERT INTO koloni2 (id, warna_lebah, status, waktu) VALUES (NULL,'hijau', 'masuk', now());"
                cursor = con.cursor()
                cursor.execute(query5)
                con.commit()
                print("masuk", yvalues_hijau)
                # print(motion_hijau)
                # print(val)

        yvalues_hijau = list()
        motion_hijau = list()
    
    # tracking warna kuning
    cnts_kuning,hierachy = cv2.findContours(kuning, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, cnts_kuning, -1, (0, 255, 0), 3)
    
    for f in cnts_kuning:
        if cv2.contourArea(f) < 100:
            continue
        (x, y, w, h) = cv2.boundingRect(f)
        yvalues_kuning.append(y)
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        flag = False
	
    no_y_kuning = len(yvalues_kuning)
    
    if (no_y_kuning > 2):
        difference_kuning = yvalues_kuning[no_y_kuning - 1] - yvalues_kuning[no_y_kuning - 2]
        if(difference_kuning > 0):
            motion_kuning.append(1)
        else:
            motion_kuning.append(0)

    if flag is True:
        if (no_y_kuning > 5):
            val, times = find_majority(motion_kuning)
            if val == 1 and times >= 10:
                count8 += 1
                query8 = "INSERT INTO koloni2 (id, warna_lebah, status, waktu) VALUES (NULL,'kuning', 'keluar', now());"
                cursor = con.cursor()
                cursor.execute(query8)
                con.commit()
                print("keluar", yvalues_kuning)
                # print(motion_kuning)
                # print(val)
                
            elif val == 0 and times >= 10:
                count7 += 1
                query7 = "INSERT INTO koloni2 (id, warna_lebah, status, waktu) VALUES (NULL,'kuning', 'masuk', now());"
                cursor = con.cursor()
                cursor.execute(query7)
                con.commit()
                print("masuk", yvalues_kuning)
                # print(motion_kuning)
                # print(val)

        yvalues_kuning = list()
        motion_kuning = list()
    
    cv2.putText(frame, "In (merah): {}".format(count1), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, "Out (merah): {}".format(count2), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, "In (biru): {}".format(count3), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, "Out (biru): {}".format(count4), (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, "In (hijau): {}".format(count5), (150, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, "Out (hijau): {}".format(count6), (150, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, "In (kuning): {}".format(count7), (150, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, "Out (kuning): {}".format(count8), (150, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Frame",frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()