# importing libraries 
import os
import shutil 
import cv2  
from PIL import Image

# Video Generating function 
def generate_video(fps): 
    print("\nCreating video from generated frames...")
    image_folder = os.listdir("test") # make sure to use your folder 
    image_folder = "test/" + image_folder[0] + "/A"
    video_name = "Real_Life_Animation.mp4"
      
    images = [img for img in os.listdir(image_folder) if (img.endswith("A2B.jpg"))]
    frame = cv2.imread(os.path.join(image_folder, images[0])) 
  
    # setting the frame width, height width the width, height of first image 
    height, width, layers = frame.shape   
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))  
  
    # Appending the images to the video one by one 
    for image in images:  
        video.write(cv2.imread(os.path.join(image_folder, image)))  
      
    # Deallocating memories taken for window creation 
    cv2.destroyAllWindows()  
    video.release()  # releasing the video generated
    print("Video created\n")

    shutil.rmtree("test", ignore_errors=True)
    shutil.rmtree("sample", ignore_errors=True)