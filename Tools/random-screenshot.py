import cv2
import os
import random

def extract_frames(vid_file, dirpath, n):
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