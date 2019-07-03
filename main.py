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
    
    # morphological transformation, opening    
    kernel = np.ones((15,15), np.float32)/255
    
    opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)
    
    # range warna yang harus dideteksi (dalam mode warna HSV)
    l_hijau = np.array([34, 50, 30])
    u_hijau = np.array([89, 255, 95])
    l_kuning = np.array([14, 110, 85])
    u_kuning = np.array([55, 255, 139])
    hijau = cv2.inRange(hsv, l_hijau, u_hijau)
    kuning = cv2.inRange(hsv, l_kuning, u_kuning)
    mask = cv2.bitwise_or(hijau, kuning)
    
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

    for i in range(len(contours)):  # looping pada semua kontur dalam frame

        if hierachy[0, i, 3] == -1:  # hierachy untuk hanya menghitung pada kontur induk

            area = cv2.contourArea(contours[i])  # luas kontur

            if minarea < area < maxarea: 
                if lineypos < cy < lineypos2:   # kirim data saat melewati area pertama
                    print(area)

                elif cy > lineypos:  # menyeleksi kontur yang sudah melewati garis

                    # mendapatkan nilai titik sudut untuk menggambar kontur persegi
                    # x,y adalah sudut kiri atas dan w,h adalah lebar dan tinggi
                    x, y, w, h = cv2.boundingRect(cnt)

                    # membuat kotak yang melingkupi setiap kontur
                    cv2.rectangle(frame, (x, y), (x + w, y + h), cv2.mean(frame, mask), 2)

    cv2.imshow("frame", frame)

    # menutup frame / program
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()