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
    u_hijau = np.array([84, 255, 99])

    # definiskan range warna kuning
    l_kuning = np.array([7, 90, 116])
    u_kuning = np.array([33, 255, 144])

    # definiskan range warna merah
    l_merah = np.array([175, 73, 71])
    u_merah = np.array([188, 156, 151])

    # definiskan range warna biru
    l_biru = np.array([97, 57, 80])
    u_biru = np.array([160, 255, 124])

    # definiskan range warna ungu
    l_ungu = np.array([158, 28, 65])
    u_ungu = np.array([201, 72, 91])

    # menemukan range warna pada citra
    hijau = cv2.inRange(hsv, l_hijau, u_hijau)
    kuning = cv2.inRange(hsv, l_kuning, u_kuning)
    merah = cv2.inRange(hsv, l_merah, u_merah)
    biru = cv2.inRange(hsv, l_biru, u_biru)
    ungu = cv2.inRange(hsv, l_ungu, u_ungu)
    
    #morphological transformation, dilation
    kernal = np.ones((5, 5), "uint8")
    
    hijau = cv2.dilate(hijau, kernal)
    res = cv2.bitwise_and(frame, frame, mask = hijau)
    
    kuning = cv2.dilate(kuning, kernal)
    res1 = cv2.bitwise_and(frame, frame, mask = kuning)
    
    merah = cv2.dilate(merah, kernal)
    res2 = cv2.bitwise_and(frame, frame, mask = merah)

    biru = cv2.dilate(biru, kernal)
    res3 = cv2.bitwise_and(frame, frame, mask = biru)

    ungu = cv2.dilate(ungu, kernal)
    res3 = cv2.bitwise_and(frame, frame, mask = ungu)

    # batas ukuran tagging yang terbaca
    minarea = 10
    maxarea = 50000
    
    # tracking warna hijau
    contours,hierachy = cv2.findContours(hijau, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    cxx = np.zeros(len(contours))
    cyy = np.zeros(len(contours))

    for i in range(len(contours)):  # looping pada semua kontur dalam frame

        if hierachy[0, i, 3] == -1:  # hierachy untuk hanya menghitung pada kontur induk

            area = cv2.contourArea(contours[i])  # luas kontur

            if minarea < area < maxarea:
                # menghitung centroid kontur
                cnt = contours[i]
                M = cv2.moments(cnt)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                if lineypos < cy < lineypos2:   # kirim data saat melewati area pertama
                    print(area)

                elif cy > lineypos:  # menyeleksi kontur yang sudah melewati garis

                    # mendapatkan nilai titik sudut untuk menggambar kontur persegi
                    # x,y adalah sudut kiri atas dan w,h adalah lebar dan tinggi
                    x, y, w, h = cv2.boundingRect(cnt)

                    # membuat kotak yang melingkupi setiap kontur
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (121,43,236), 2)
    
    # tracking warna kuning
    contours,hierachy = cv2.findContours(kuning, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    cxx = np.zeros(len(contours))
    cyy = np.zeros(len(contours))

    for i in range(len(contours)):  # looping pada semua kontur dalam frame

        if hierachy[0, i, 3] == -1:  # hierachy untuk hanya menghitung pada kontur induk

            area = cv2.contourArea(contours[i])  # luas kontur

            if minarea < area < maxarea:
                # menghitung centroid kontur
                cnt = contours[i]
                M = cv2.moments(cnt)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                if lineypos < cy < lineypos2:   # kirim data saat melewati area pertama
                    print(area)

                elif cy > lineypos:  # menyeleksi kontur yang sudah melewati garis

                    # mendapatkan nilai titik sudut untuk menggambar kontur persegi
                    # x,y adalah sudut kiri atas dan w,h adalah lebar dan tinggi
                    x, y, w, h = cv2.boundingRect(cnt)

                    # membuat kotak yang melingkupi setiap kontur
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (121,43,236), 2)

    # tracking warna merah
    contours,hierachy = cv2.findContours(merah, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    cxx = np.zeros(len(contours))
    cyy = np.zeros(len(contours))

    for i in range(len(contours)):  # looping pada semua kontur dalam frame

        if hierachy[0, i, 3] == -1:  # hierachy untuk hanya menghitung pada kontur induk

            area = cv2.contourArea(contours[i])  # luas kontur

            if minarea < area < maxarea:
                # menghitung centroid kontur
                cnt = contours[i]
                M = cv2.moments(cnt)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                if lineypos < cy < lineypos2:   # kirim data saat melewati area pertama
                    print(area)

                elif cy > lineypos:  # menyeleksi kontur yang sudah melewati garis

                    # mendapatkan nilai titik sudut untuk menggambar kontur persegi
                    # x,y adalah sudut kiri atas dan w,h adalah lebar dan tinggi
                    x, y, w, h = cv2.boundingRect(cnt)

                    # membuat kotak yang melingkupi setiap kontur
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (121,43,236), 2)
    
    # tracking warna biru
    contours,hierachy = cv2.findContours(biru, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    cxx = np.zeros(len(contours))
    cyy = np.zeros(len(contours))

    for i in range(len(contours)):  # looping pada semua kontur dalam frame

        if hierachy[0, i, 3] == -1:  # hierachy untuk hanya menghitung pada kontur induk

            area = cv2.contourArea(contours[i])  # luas kontur

            if minarea < area < maxarea:
                # menghitung centroid kontur
                cnt = contours[i]
                M = cv2.moments(cnt)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                if lineypos < cy < lineypos2:   # kirim data saat melewati area pertama
                    print(area)

                elif cy > lineypos:  # menyeleksi kontur yang sudah melewati garis

                    # mendapatkan nilai titik sudut untuk menggambar kontur persegi
                    # x,y adalah sudut kiri atas dan w,h adalah lebar dan tinggi
                    x, y, w, h = cv2.boundingRect(cnt)

                    # membuat kotak yang melingkupi setiap kontur
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (121,43,236), 2)

    # tracking warna ungu
    contours,hierachy = cv2.findContours(ungu, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    cxx = np.zeros(len(contours))
    cyy = np.zeros(len(contours))

    for i in range(len(contours)):  # looping pada semua kontur dalam frame

        if hierachy[0, i, 3] == -1:  # hierachy untuk hanya menghitung pada kontur induk

            area = cv2.contourArea(contours[i])  # luas kontur

            if minarea < area < maxarea:
                # menghitung centroid kontur
                cnt = contours[i]
                M = cv2.moments(cnt)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                if lineypos < cy < lineypos2:   # kirim data saat melewati area pertama
                    print(area)

                elif cy > lineypos:  # menyeleksi kontur yang sudah melewati garis

                    # mendapatkan nilai titik sudut untuk menggambar kontur persegi
                    # x,y adalah sudut kiri atas dan w,h adalah lebar dan tinggi
                    x, y, w, h = cv2.boundingRect(cnt)

                    # membuat kotak yang melingkupi setiap kontur
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (121,43,236), 2)

    cv2.imshow("frame", frame)

    # menutup frame / program
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()