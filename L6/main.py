import cv2
import os
from PIL import Image

# os.chdir("")
path = "/Users/onorenosenathanikhuoria/Desktop/Open CV/L6/images"
mean_height = 0
mean_width = 0
numofimages = len(os.listdir(path))
for file in os.listdir(path):
    img = Image.open(os.path.join(path, file))
    width, height = (img.size)
    mean_width = mean_width + width
    mean_height = mean_height + height
mean_width = mean_width // numofimages
mean_height = mean_height // numofimages
print(mean_width)
print(mean_height)
for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith(".jpeg)") or file.endswith(".png"):
        img = Image.open(os.path.join(path, file))
        wdith, height = (img.size)
        print(width, height)
        img_resized = img.resize((mean_width, mean_height,), Image.Resampling.LANCZOS)
        img_resized.save(file, 'JPEG', quality = 95)
        print(img.filename.split('\\')[-1], "is resized")