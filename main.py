import cv2
import numpy as np
from matplotlib import pyplot as plt
import imageio
import re
import os
import sys
import glob

# read_path = './14'
# store_path = './covered_14'
# pattern = '(?:[(\)/]+)|[0-9]+|(?:[(\)/]+)|(?:[\w]+)'

# def create_dir(dir_path):
#     if not os.path.exists(dir_path):
#         os.makedirs(dir_path)

# def main():
#     create_dir(store_path)
#     for dir_path in os.listdir(read_path):
#         path = './14'
#         path = path + "/" + dir_path
#         create_dir(store_path + "/" + dir_path)
#         for filename_path in glob.glob(os.path.join(path, '*.png')):
#             print(filename_path)
#             img = imageio.imread(filename_path)
#             filename = re.findall(pattern,filename_path)
#             try:
#                 img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#             except cv2.error as e:
#                 cv2.imwrite(store_path + "/" + dir_path + "/" + filename[4] +'.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 5])
#                 continue
                
#             plt.imshow(img_hsv)   
#             plt.show()
#             hsv_color1 = np.asarray([103, 34, 255]) 
#             hsv_color2 = np.asarray([103, 35, 255]) 

#             mask = cv2.inRange(img_hsv, hsv_color1, hsv_color2)
#             # cv2.imwrite(store_path + "/" + dir_path + "/" + filename[4] +'.png', img_gray , [cv2.IMWRITE_PNG_COMPRESSION, 5])

#             plt.imshow(mask, cmap='gray')   # this colormap will display in black / white
#             plt.axis('off')
#             plt.savefig('fig.png', bbox_inches='tight')
#             plt.show()



# if __name__ == "__main__":
#     main()

#     sys.exit(0)

img = imageio.imread("./14/13668\map_13668_7135_14.png")
plt.imshow(img)   
plt.show()
try:
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
except cv2.error as e:
    print("1212")

plt.imshow(img_hsv)   
plt.show()
hsv_color1 = np.asarray([103, 33, 255]) 
hsv_color2 = np.asarray([104, 33, 255]) 

mask = cv2.inRange(img_hsv, hsv_color1, hsv_color2)

plt.imshow(mask, cmap='gray')   # this colormap will display in black / white
plt.axis('off')
plt.savefig('fig.png', bbox_inches='tight')
plt.show()