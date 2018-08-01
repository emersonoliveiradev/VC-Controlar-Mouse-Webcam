import numpy as np
import cv2
import os



font = cv2.FONT_HERSHEY_COMPLEX_SMALL
hand_detection = cv2.CascadeClassifier("haar_cascade_hand.xml")
#hand_detection = cv2.CascadeClassifier("haar_cascade_finger.xml")
cap = cv2.VideoCapture(1)

def mouse_mov(x, y):
    os.system("xdotool mousemove " + str(int(x*3.5)) + " " + str(int(y*3.5)))

def mouse_click_1(x, y):
    os.system("xdotool mousemove " + str(int(x*2.5)) + " " + str(int(y*2.0)) + " click 1")

def mouse_double_click_1(x, y):
    os.system("xdotool mousemove " + str(int(x*2.5)) + " " + str(int(y*2.0)) + " click 1 click 1")

def mouse_click_2(x, y):
    os.system("xdotool mousemove " + str(int(x*2.5)) + " " + str(int(y*2.0)) + " click 2")

def mouse_click_3(x, y):
    os.system("xdotool mousemove " + str(int(x*2.5)) + " " + str(int(y*2.0)) + " click 3")


while(True):
    ret, frame =  cap.read()
    if ret == False:
        print("Turn on your camera!")
        break

    frame_gray = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)

    hand_detected = hand_detection.detectMultiScale(frame_gray, scaleFactor=1.5, minSize=(50,50))
    for (x, y, l, a) in hand_detected:
        #cv2.circle(frame, (x, y), 35, (255, 0, 0), -1)
        img = cv2.rectangle(frame_gray.copy(), (x, y), (x + l, y + a), (0, 0, 255), 2)
        mouse_mov(x, y)
        cv2.circle(frame, (int((x+x+l)/2), int((y+y+a)/2)), 5, (0, 0, 255), -1)

        ret, thresh = cv2.threshold(img, 127, 255, 0)
        #cv2.imshow("Capture2", img)
        #cv2.imshow("tresh", thresh)

    cv2.imshow("Capture", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

