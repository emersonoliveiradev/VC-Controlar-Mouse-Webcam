import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while( True ) :
    ret , frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    ret, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    (_, contours, hierarchy) = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areas = [cv2.contourArea(temp) for temp in contours]
    max_index = np.argmax(areas)
    largest_contour = contours[max_index]
    approx = cv2.approxPolyDP(largest_contour, 0.01 * cv2.arcLength(largest_contour, True), True)
    hull = cv2.convexHull(approx, returnPoints=True)
    cv2.putText(frame, 'Number of Fingers ' + str(len(hull) - 2), (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                (255, 0, 0))
    cv2.drawContours(frame, [hull], 0, (0, 0, 255), 1)
    for i in range(len(hull)):
        [x, y] = hull[i][0].flatten()
        cv2.circle(frame, (int(x), int(y)), 2, (0, 255, 0), -1)
        cv2.circle(frame, (int(x), int(y)), 5, (255, 255, 0), 1)
        cv2.circle(frame, (int(x), int(y)), 8, (255, 0, 0), 1)

    print("Number of Fingers " + str((len(hull) - 2)))
    cv2.imshow('Gestures', frame)

    if cv2.waitKey(5) == 27:
        break

cv2.destroyAllWindows()
cap.release()