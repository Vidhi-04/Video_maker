import os
import cv2


path = "Images"
images = []

listOfImages = os.listdir(path)

for x in listOfImages :
    name, extension =os.path.splitext(x)
    if extension in [".jpg"] :
        images.append(path+"/"+name+extension)
print(len(images)) 

count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)
print(size)

out = cv2.VideoWriter("Photo_Album.mp4", cv2.VideoWriter_fourcc(*'DIVX'),
0.8, size)

for i in range (count-1, 0, -1):
    video = cv2.imread(images[i])
    out.write(video)
out.release()
print("done")    