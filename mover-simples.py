import cv2
import numpy as np

ball = cv2.imread("ball.jpg")
ball = cv2.resize(ball, None, fx=0.1, fy=0.1, interpolation = cv2.INTER_LINEAR)
rows, cols, channels = ball.shape


cap = cv2.VideoCapture(1)


while(True):
    ret, frame = cap.read()
    if ret == False:
        print("Turn on your camera!")

    #roi = frame[0:rows, 0:cols]

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #"Borra" a imagem, mais f[acil pro computador encontrar depois os limiares
    frame_blur = cv2.GaussianBlur(frame_gray, (5, 5), 0)

    _, thresh1 = cv2.threshold(frame_blur, 20, 255, (cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU))



    add_image = cv2.add(frame, frame)

    cv2.imshow("Frame", frame)
    cv2.imshow("Gray", frame_gray)
    cv2.imshow("Blur", frame_blur)
    cv2.imshow("Frame2", add_image)

    cv2.moveWindow("Frame", 0 , 50)
    cv2.moveWindow("Gray", 700, 50)
    cv2.moveWindow("Blur", 1400, 50)


    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    else:
        pass

cap.release()
cv2.destroyAllWindows()

