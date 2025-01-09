# Perspective transformation logic inspired by [Adrian Rosebrock](https://pyimagesearch.com)

#all the libraries im going to need
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.filters import threshold_local 
#worry about this library later
from PIL import Image
import os


#ask the user which image they want to use out of the images folder i have

image_folder = "images"

all_files = sorted(os.listdir(image_folder))

images = []
for file in all_files:
    if file.endswith(".jpg"): #only put the jpegs
        images.append(file)

#show the user availble images
print("Available Receipts:")
images.sort()
print(images)
for i in range(len(images)):
    print(f"{i}. {images[i]}")

choice = int(input("Enter which images you want to use: "))


selected_image = images[choice]
file_path = (os.path.join(image_folder, selected_image))
img = Image.open(file_path)


#rescale to for efficeincy while keeping it a relatively high quality image
img.thumbnail((800, 800), Image.Resampling.LANCZOS)


#utitlity functions to resize
def opencv_resize(image, ratio):
    width = int(image.shape[1] * ratio)
    height = int(image.shape[0] * ratio)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

#change from bgr to rgb
def plot_rgb(image):
    plt.figure(figsize=(16,10))
    return plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) 

#grayscale conversiono
def plot_gray(image):
    plt.figure(figsize=(16,10))
    return plt.imshow(image, cmap='Greys_r')

#load in th eimage with open cv and then resize it 
image = cv2.imread(file_path)
resize_ratio = 500 / image.shape[0]
original = image.copy()
image = opencv_resize(image, resize_ratio)

#convert to gray and then show what it looks like in gray 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# get rid of noise with Gaussian Blur filter
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# ok so to put this into simple terms it finds the white regions of the image and then enlarges them so you see more white eseentially dilating them
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
dilated = cv2.dilate(blurred, rectKernel)

# uses canny edge detectino to find the eges of the receipt
edged = cv2.Canny(dilated, 100, 200, apertureSize=3)

# detect all contours in Canny-edged image
contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image_with_contours = cv2.drawContours(image.copy(), contours, -1, (0,240,0), 3)
# plot_rgb(image_with_contours)
# plt.show()


#get onnly the 10 biggest contours by area  adn then draw thme
largest_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
image_with_largest_contours = cv2.drawContours(image.copy(), largest_contours, -1, (0, 255, 0), 3)

# approximate the contour by a more primitive polygon shape
def approximate_contour(contour):
    peri = cv2.arcLength(contour, True)
    return cv2.approxPolyDP(contour, 0.032 * peri, True)

def get_receipt_contour(contours):    
    # loop over the contours
    for c in contours:
        approx = approximate_contour(c)
        # if our approximated contour has four points, we can assume it is receipt's rectangle
        if len(approx) == 4:
            return approx

get_receipt_contour(largest_contours)

receipt_contour = get_receipt_contour(largest_contours)
image_with_receipt_contour = cv2.drawContours(image.copy(), [receipt_contour], -1, (0, 255, 0), 2)
plot_rgb(image_with_receipt_contour)
plt.show()