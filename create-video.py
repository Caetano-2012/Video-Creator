import cv2
import os

path = "images"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    file_name = path + "/" + file
    print(file_name)

    images.append(file_name)

print(len(images))

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)
print(size)