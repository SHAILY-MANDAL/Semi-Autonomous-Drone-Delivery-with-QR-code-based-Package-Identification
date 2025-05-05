GNU nano 5.4

Import cv2

import numpy as np

import pyzbar.pyzbar as qr

cap = cv2.VideoCapture (0)

font= cv2.FONT HERSHEY PLAIN

if not cap.isopened():

print("fail")

exit

while True:

ret, frame cap.read()

if not ret:

print("hi")

break

flipped = cv2.flip(frame, flipcode = -1) framel = cv2.resize(flipped, (640,480))

grdetect = gr.decode (frame1)

I

for i in grdetect:

print(i.rect.left,i.rect.top,i.rect.width,i.rect.height) print(i.data)

cv2.rectangle(frame1, (i.rect.left,i.rect.top), (i.rect.left+i.rect.width, i.rect.top+i.rect.height),

(0,255,0),3) cv2.putText(framel,str(i.data), (20,20), font, 2, (255,0,0),2)

cv2.imshow("Frame",frame1) key= cv2.waitKey(1) & 0xFF

if key ord("g");

break