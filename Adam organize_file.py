import cv2
import os
import random
# test data set with some of my flosports work videos (34 files)
import r'G:\Other computers\USB and External Devices\USB_DEVICE_1697923505\PRIVATE\AVCHD\BDMV\STREAM'


def organize_file(vid_file, actor_name)
    #opens the video file
    cap = cv2.VideoCapture(vid_file)

    #variable will become true if the actor is in the video
    found = False

    new_name = actor_name
    
    while not Found
       
        extract_frames(vid_file, dirpath, n)
        if frames.contains(actor_name)
           
            #will create a new folder with the actor name if none already exists and place the video file in it
            
            newpath = r'C:\Users\abend\OneDrive\Desktop\Computing Club\WhichBatman\new_name'
           
            if not os.path.exists(newpath):
                os.makedirs(newpath)            
                Found = True

def main()
    # testing organize file method on the flosports/milesplit videos--
    organize_file(G:\Other computers\USB and External Devices\USB_DEVICE_1697923505\PRIVATE\AVCHD\BDMV\STREAM\00000, "Adam West")
    organize_file(G:\Other computers\USB and External Devices\USB_DEVICE_1697923505\PRIVATE\AVCHD\BDMV\STREAM\00010, "Christian Bale")
    organize_file(G:\Other computers\USB and External Devices\USB_DEVICE_1697923505\PRIVATE\AVCHD\BDMV\STREAM\00020, "Ben Affleck")
    organize_file(G:\Other computers\USB and External Devices\USB_DEVICE_1697923505\PRIVATE\AVCHD\BDMV\STREAM\00030, "Your Mom")
