import cv2 

def play_video_from_url(url):
    cap = cv2.VideoCapture(url)

    # check if url was opened
    if not cap.isOpened():
        print('video not opened')
        exit(-1)

    while True:
        # read frame
        ret, frame = cap.read()

        # check if frame is empty
        if not ret:
            break

        # display frame
        cv2.imshow('frame', frame)

        if cv2.waitKey(30)&0xFF == ord('q'):
            break

    # release VideoCapture
    cap.release()
    cv2.destroyAllWindows()
