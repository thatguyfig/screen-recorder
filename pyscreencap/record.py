import cv2
import numpy as np
import os
import pyautogui
import time
from datetime import datetime
from config import *

def generate_filename():
    # generate datetime
    now = datetime.now()
    new_now = now.strftime("%d-%m-%Y_%H-%M-%S")
    return new_now

def make_directories():
    # create the output directory
    if not os.path.exists(os.environ['USERPROFILE'] + '\\pyscreencap-recordings'):
        os.makedirs(os.environ['USERPROFILE'] + '\\pyscreencap-recordings')

def make_video_writer():
    # display screen resolution
    SCREEN_SIZE = pyautogui.size()

    # define the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")

    # build output path filename
    output_path = os.environ['USERPROFILE'] + '\\pyscreencap-recordings\\{}.avi'.format(generate_filename())
    
    # create the video writer object
    out = cv2.VideoWriter(output_path, fourcc, RECORDING_FPS, (SCREEN_SIZE))

    return out

    
def start_recording(video_writer):
    paused = False
    flipper = -1

    # start iterating
    while True:

        if paused == False:
            # take a screenshot
            img = pyautogui.screenshot()

            # convert these pixels to a proper numpy array to work with OpenCV
            frame = np.array(img)

            # convert colors from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # write the frame
            video_writer.write(frame)

            # show the frame
            cv2.imshow("screenshot", frame)

        # if the user hits p , pause
        if cv2.waitKey(1) == ord("p"):

            # flip the flipper
            flipper = flipper * -1

            # if paused
            if flipper == 1:
                pyautogui.alert('Paused.')
                paused == True
            else:
                pyautogui.alert('Playing.')
                paused == False
            time.sleep(1)


        # if the user hits q , close
        if cv2.waitKey(1) == ord("q"):
            break


    # make sure everything is closed
    cv2.destroyAllWindows()
    video_writer.release()

def main():

    print('PyScreenRecorder...')
    print('Recordings saved under:',os.environ['USERPROFILE'] + '\\pyscreencap-recordings\\' )
    print('Press "p" to pause & hold "q" to quit.')



    # make required output path
    make_directories()

    # generate filename and writer
    out = make_video_writer()

    # start recording
    start_recording(video_writer=out)

def run():
    main()

if __name__ == "__main__":
    main()