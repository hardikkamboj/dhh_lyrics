import cv2 
from video_lyrics_module import *

lyrics = []

def play_video(address):

    cap = cv2.VideoCapture(address)

    # check if url was opened
    if not cap.isOpened():
        print('video not opened')
        exit(-1)

    c = 1
    while True:
        # read frame
        ret, frame = cap.read()
        c+=1

        if c%5!=0:
            continue
        
        # check if frame is empty
        if not ret:
            break

        # converting to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        threshold_value = 0.85
        bottom_value = int(threshold_value * gray.shape[0])

        # display frame
        cv2.imshow('frame', frame)

        #diplay the lyrics 
        cv2.imshow('lyrics',gray[bottom_value:,:])

        text = get_text_from_image(gray[bottom_value:,:])

        if len(text) > 0:
            if lyrics == []:
                lyrics.append(text)
                print(text)
            
            elif text != lyrics[-1]:
                lyrics.append(text) 
                print(text)           

        if cv2.waitKey(30)&0xFF == ord('q'):
            break
    

    # release VideoCapture
    cap.release()
    cv2.destroyAllWindows()
    
