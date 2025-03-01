import cv2 as cv

capture = cv.VideoCapture('Inputs/Videos/RnB_Example.mp4')

while True:
    isTrue, frame = capture.read()

    # shows video
    cv.imshow('Video', frame)

    #hit D key to stop video
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()