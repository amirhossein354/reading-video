import cv2

cap = cv2.VideoCapture("video.mp4")
if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame', frame)
            key = cv2.waitKey(20)
            if key != -1:
                print("video quited")
                break
        else:
            print("video finished")
            break
    cv2.destroyAllWindows()
    cap.release()
else:
    print("video not opened")
