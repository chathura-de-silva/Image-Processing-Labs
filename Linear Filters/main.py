import numpy as np;
import cv2 as cv;
from os import path

def normalize_filter(filter_array):
    return filter_array/np.sum(np.abs(filter_array))

# Filter 1 (Filter A) - Laplacian of Gaussian (LoG) Filter
filter1 = normalize_filter(np.array([
    [0, -1, -1, -1, 0],
    [-1, 2, 2, 2, -1],
    [-1, 2, 8, 2, -1],
    [-1, 2, 2, 2, -1],
    [0, -1, -1, -1, 0]
]))

# Filter 2 (Filter B) - Gaussian Blur Filter
filter2 = normalize_filter(np.array([
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1]
]))

# Filter 3 (Filter C) - Uniform Box Filter
filter3 = normalize_filter(np.array([
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5]
]))

# Filter 4 (Filter D) - Sharpening Filter (High-Boost Filter)
filter4 = normalize_filter(np.array([
    [0, -1, -1, -1, 0],
    [-1, 2, 2, 2, -1],
    [-1, 2, 16, 2, -1],
    [-1, 2, 2, 2, -1],
    [0, -1, -1, -1, 0]
]))



#  Reading the image using OpenCV. Handled file not found situation.

img = cv.imread('./road98.png')
if img is None:
    print("Error: Image not found.")
    exit()
print(f"Image converted to type : {type(img)}" )

#  Converting the 3D Numpy Array containing BGR Image to a 2D array containing the Grayscale Image.

gray_img = np.round(0.114 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.299 * img[:, :, 2]).astype(np.uint8)

max_val= np.max(gray_img)
min_val = np.min(gray_img)

original_img = np.round(255*((gray_img-min_val)/(max_val-min_val))).astype(np.uint8);
cv.imwrite('./original.jpg',original_img ) # Saving as an image.

# Adding padding.
filter_offset = filter1.shape[0]//2  # Offset for the filter.
print(filter_offset)
for i in range(filter_offset) :
    if i==0:
        padded_img = np.insert(original_img, 0, 0, axis=0)
    else: 
         padded_img = np.insert(padded_img, 0, 0, axis=0)
    padded_img = np.insert(padded_img[::-1],0 , 0, axis=0)
    padded_img = np.insert(padded_img, 0, 0, axis=1)
    padded_img = np.insert(padded_img, padded_img.shape[1], 0, axis=1)
print(padded_img)
# print()
print(original_img.shape)
print(padded_img.shape)

def apply_filter_and_save_image(img_filter, img_name):
    new_img = np.zeros_like(original_img)
    for i in range(original_img.shape[0]):
        for j in range(original_img.shape[1]):
            new_img[i][j] = np.sum(padded_img[i:i+img_filter.shape[0], j:j+img_filter.shape[1]] * img_filter)
    print(new_img)
    cv.imwrite('./'+img_name,new_img ) # Saving as an image.

apply_filter_and_save_image(filter1, 'filterA.jpg')
apply_filter_and_save_image(filter2, 'filterB.jpg')
apply_filter_and_save_image(filter3, 'filterC.jpg')
apply_filter_and_save_image(filter4, 'filterD.jpg')

def calcRms(original, edited):
    return np.sqrt(np.mean(np.square(original - edited)))

print(f"RMS for Filter A: {calcRms(original_img, cv.imread('./filterA.jpg', cv.IMREAD_GRAYSCALE))}")
print(f"RMS for Filter B: {calcRms(original_img, cv.imread('./filterB.jpg', cv.IMREAD_GRAYSCALE))}")
print(f"RMS for Filter C: {calcRms(original_img, cv.imread('./filterC.jpg', cv.IMREAD_GRAYSCALE))}")
print(f"RMS for Filter D: {calcRms(original_img, cv.imread('./filterD.jpg', cv.IMREAD_GRAYSCALE))}")