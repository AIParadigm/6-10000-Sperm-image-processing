from PIL import Image
import os
path = 'F:/ultralytics-main/datasets/sperm/images/train2017'
file_list = os.listdir(path)
for file in file_list:
    I = Image.open(path+"/"+file)
    L = I.convert('L')
    L.save(path+"/"+file)
