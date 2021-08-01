# -*- coding: utf-8 -*-
import requests
import time
import cv2

#ラズパイに接続したカメラで撮影
camera = cv2.VideoCapture(0)
ret, frame = camera.read()
cv2.imwrite("win2.jpg", frame)

#LINE Notifyの定義
url = "https://notify-api.line.me/api/notify"
access_token = 't9Q0Teu3IcF7WjOOuCBaIgDuDFNRQshvrLLLNUcYrN4'
headers = {'Authorization': 'Bearer ' + access_token}

#LINE Notifyにメッセージと画像を送信
message = 'ゴリラの写真'
image = 'seta.jpeg'  # png or jpg
payload = {'message': message}
files = {'imageFile': open(image, 'rb')}
r = requests.post(url, headers=headers, params=payload, files=files,)