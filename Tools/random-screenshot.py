import cv2
import os
import random

def extract_frames(vid_file, dirpath, n):
    """
    Args:
        vid_file: path of mp4 video file  (String)
        dirpath: path of images output (String)
        n: the number of frames genorated
    Shape:
        Input: (vid_file, dirpath, n).
        Output: stores n number of random frames from vid_file to the dirpath
        frames are named "frame_#" # meaning which frame out of n it is starting at 0
        lastly prints "All frames extracted" when it is finished.
    Example:
        Input: extract_frames("C:\TestFolder\BatmanScene.mp4","C:\TestFolder\FramesFolder", 10)
        Output: 10 random frames from "BatmanScene" will be saved to "FramesFolder"
    """
    #Creates a directory if it does not exist at dirpath
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    #Open the vid_file
    cap = cv2.VideoCapture(vid_file)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    #Creates a list of random frame #'s
    random_frame_nums = random.sample(range(total_frames), n)
    for i, frame_num in enumerate(random_frame_nums):
        #Sets the postition  of the video capture to the selected frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        
        #Read and save the frame
        ret, frame = cap.read()
        if not ret:
            continue
        
        #Saves the frame as a image
        frame_filename = os.path.join(dirpath, f"frame_{i}.jpg")
        cv2.imwrite(frame_filename, frame)

    #Stops the capture
    cap.release()
    print("All frames extracted")