import cv2
img=cv2.imread('./Solar-system.jpg')
cv2.putText(img,
            "Sun",
            (90,90),
            cv2.FONT_HERSHEY_COMPLEX,
            0.9,
            (255,255,255))
cv2.putText(img,
            "Mercury",
            (110,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Venus",
            (190,160),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Earth",
            (290,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Mars",
            (385,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Jupiter",
            (585,380),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Saturn",
            (775,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Uranus",
            (965,290),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Neptune",
            (1110,145),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.imwrite("Solar System with name.jpg",img)