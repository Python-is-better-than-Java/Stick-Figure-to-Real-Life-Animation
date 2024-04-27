import cv2
import os

# Frame generating function
def vid_to_frame():

    # find the stick-figure animation video
    files = os.listdir('.')
    video = [vid for vid in files if (vid.endswith(".mp4"))]

    cam = cv2.VideoCapture(video[0])
    fps = cam.get(cv2.CAP_PROP_FPS)
    currentframe = 1000
    print ("Creating frames from stick-figure animation...") 

    while(True): 
        
        # reading from frame 
        ret,frame = cam.read() 

        if ret: 
            # if video is still left continue creating images
            name = "datasets/sketch-photo/val/A/" + "A_" + str(currentframe) + ".jpg"

            # writing the extracted images 
            cv2.imwrite(name, frame) 

            # increasing counter so that it will show how many frames are created 
            currentframe += 1
        else: 
            break
    
    print("Frames created\n")
    return fps

# Frame removal function
def rem_frames():
    files = os.listdir("datasets/sketch-photo/val/A")
    
    for img in files:
        if (img.endswith(".jpg")):
            os.remove("datasets/sketch-photo/val/A/" + img)