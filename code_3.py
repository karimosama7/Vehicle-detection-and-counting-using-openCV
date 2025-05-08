import cv2
import numpy as np


def center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1

    return cx, cy


decte = []
count = 0

cap = cv2.VideoCapture("video.mp4")

subtracao = cv2.bgsegm.createBackgroundSubtractorMOG()


while cap.isOpened():
    _, frame1 = cap.read()
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 5)
    bsg = subtracao.apply(blur)
    dilted = cv2.dilate(bsg, np.ones((5, 5)))

    conturs, _ = cv2.findContours(dilted, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cv2.line(frame1, (25, 550), (1150, 550), (100, 150, 50), 3)
    for i, c in enumerate(conturs):
        (x, y, w, h) = cv2.boundingRect(c)
        vaild = (w >= 80) and (h >= 80)
        if not vaild:
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + w), (0, 255, 0), 2)
        centors = center(x, y, w, h)
        decte.append(centors)
        cv2.circle(frame1, centors, 5, (0, 0, 255), -1)

        for x, y in decte:
            if (y < 550 + 6) and (y > 550 - 6):
                count += 1
                cv2.line(frame1, (25, 550), (1150, 550), (0, 100, 255), 3)
                decte.remove((x, y))
    cv2.putText(
        frame1,
        "VEHICLE COUNT : " + str(count),
        (320, 70),
        cv2.FONT_HERSHEY_COMPLEX,
        2,
        (0, 0, 255),
        4,
    )

    cv2.imshow("frame", frame1)
    # cv2.imshow("diltaed", dilted)

    if cv2.waitKey(60) == 27:
        break

cv2.destroyAllWindows()
cap.release()
