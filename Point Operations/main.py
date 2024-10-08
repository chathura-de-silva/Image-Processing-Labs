import numpy as np;
import cv2 as cv;
import matplotlib.pyplot as plt
from os import path

#  Reading the image using OpenCV. Handled file not found situation.

img = cv.imread('./assets/inputImg1.jpg')
if img is None:
    print("Error: Image not found.")
    exit()
print(f"Image converted to type : {type(img)}" )

#  Converting the 3D Numpy Array containing BGR Image to a 2D array containing the Grayscale Image.

gray_img = np.round(0.114 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.299 * img[:, :, 2]).astype(np.uint8)

# Displaying and Exporting Grayscale Image. (Exporting uses OpenCV.)

plt.imshow(gray_img, cmap='gray')
plt.title('Grayscale Image')
plt.show()

# Manipulating the grayscale image applying required point operations.
# `low_bpp_img` now has now 4 bit data logically. 
# When plotting the low bpp one, will have to scale this back to 0-255. Still the image will only have 4 bit worth actual data.

negative_img = 255-gray_img;
bright_img = np.clip(np.round(gray_img.astype(np.uint16) * 1.2), 0, 255).astype(np.uint8); # Avoiding overflow by converting to uint16
low_contrast_img = np.round(125+ ((10/51)*gray_img)).astype(np.uint8);
low_bpp_img = np.floor(gray_img/(16)).astype(np.uint8);  
vertical_mirror_img = np.array([arr[::-1] for arr in gray_img])

# Displaying all the Numpy 2D arrays as Grayscale Images with titles.

fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(6, 14));
axs[0,0].imshow(gray_img, cmap="gray", vmin=0,vmax=255);
axs[1,0].imshow(negative_img, cmap="gray", vmin=0,vmax=255);
axs[2,0].imshow(bright_img, cmap="gray", vmin=0,vmax=255);
axs[0,1].imshow(low_contrast_img, cmap="gray", vmin=0,vmax=255);
axs[1,1].imshow(low_bpp_img*(255/15), cmap="gray", vmin=0,vmax=255);
axs[2,1].imshow(vertical_mirror_img,cmap="gray", vmin=0,vmax=255 );


axs[0,0].set_title("Grayscale Unprocessed");
axs[1,0].set_title("Negative");
axs[2,0].set_title("Brightness Increased");
axs[0,1].set_title("Low Contrast");
axs[1,1].set_title("Low BPP");
axs[2,1].set_title("Vertical Mirror");

# Saving images
cv.imwrite('./assets/subPlot11.jpg',gray_img ) # Saving as an image.
cv.imwrite('./assets/subPlot12.jpg',negative_img ) # Saving as an image.
cv.imwrite('./assets/subPlot13.jpg',bright_img ) # Saving as an image.
cv.imwrite('./assets/subPlot21.jpg',low_contrast_img ) # Saving as an image.
cv.imwrite('./assets/subPlot22.jpg',low_bpp_img*(255/15) ) # Saving as an image. # Scaled 4 bit data to 8 bit.
cv.imwrite('./assets/subPlot23.jpg',vertical_mirror_img ) # Saving as an image.

plt.show();
