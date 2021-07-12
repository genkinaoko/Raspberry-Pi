# -*- coding: utf-8 -*-
import cv2
import subprocess, shlex
import requests
import os
import time

cap = cv2.VideoCapture(0)
cmd = shlex.split("./alexa_remote_control.sh -e \"speak:こんにちは、高崎さんは外出中です\"")
#cmd2 = shlex.split("./alexa_remote_control.sh -e \"speak:今日は午後５時に帰ってくると伺っております。\"")
key = True
key2 = True
time2 = 0
before = None

#LINE Notifyの定義
url = "https://notify-api.line.me/api/notify"
access_token = 't9Q0Teu3IcF7WjOOuCBaIgDuDFNRQshvrLLLNUcYrN4'
headers = {'Authorization': 'Bearer ' + access_token}

time.sleep(10)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (int(frame.shape[1]), int(frame.shape[0])))
    #cv2.imshow("No process", frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if before is None:
        before = gray.copy().astype("float")
        continue
    cv2.accumulateWeighted(gray, before, 0.5)
    mdframe = cv2.absdiff(gray, cv2.convertScaleAbs(before))

    #cv2.imshow("motion detcted", mdframe)
    thresh = cv2.threshold(mdframe, 3, 255, cv2.THRESH_BINARY)[1]
    image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    target = contours[0]
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if max_area < area and area < 10000 and area > 1000:
            max_area = area
            target = cnt
    if max_area <= 1000:
        areaframe = frame
        cv2.putText(areaframe, "not detected", (0,50), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3, cv2.LINE_AA)
        time2 = 0
    else:
        x,y,w,h = cv2.boundingRect(target)
        areaframe = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        time2 += 1
    
    cv2.imshow("Motion detected", areaframe)
    if time2 >= 15 and key:
        res = subprocess.call(cmd)
        time2 = 0
        key = False
        cv2.imwrite("pre.jpg", frame)
        #LINE Notifyにメッセージと画像を送信
        message = '室内に移動物体を検知しました。'
        image = 'pre.jpg'  # png or jpg
        payload = {'message': message}
        files = {'imageFile': open(image, 'rb')}
        r = requests.post(url, headers=headers, params=payload, files=files,)
        os.remove("pre.jpg")

    k = cv2.waitKey(1)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

