![banner](./banner.png)
*   This repository contains Lab exercises covered under " CS3713-Image Processing" module in semester 5, UOM CSE, which had coding involved.


## Point Operations

A Python script to carry out the following operations:

1. Loading a colour image (in JPG or PNG format) from the disk and convert the image to 8-bpp grayscale format.

2. Creating a 3x2 sub-plot and display the gray-scale image and output images images  in different grid positions as follows.

*   grid (1,1) :  unprocessed gray-scale image
*   grid (1,2): negative image
*   grid (1,3): increased brightness by 20% on each pixel
*   grid (2,1): Reduce image contrast such that gray levels remain between 125 and 175
*   grid (2,2): Reduce image gray level depth to 4bpp from 8 bpp
*   grid (2,3): Vertical mirror image of the unprocessed image


(OpenCV library, only for loading the source image and saving your output.  No other libraries (except for matplotlib, numpy)).

### Instructions for Running
* Python version 3.12 is recommended. Install the dependencies from `requirements.txt`.

*   There are two versions with more or less the same code.
    1. Jupyter Notebook Version
    2. Regular `.py` Script.

*   Put the preffered image inside `/assets` directory. 
*   Change the image path in the python code or just rename your image as `inputImg1.jpg`.
*   If you are running the python script, make sure to cd in to the `/Point Operations` or change the image path accordingly. Otherwise the script will fail with `Error: Image not found.` message.
*   You may have to adjust the `figsize` parameter of the code which specifies figure width and height respectively according to your input image aspect ratio.

<p align="center"><img src="./Point Operations/assets/inputImg1.jpg" width=150></p>
<table>
    <tr>
        <td><img src="./Point Operations\assets\subPlot11.jpg" alt="Image 1" width="1600"></td>
        <td><img src="./Point Operations\assets\subPlot12.jpg" alt="Image 2" width="1600"></td>
        <td><img src="./Point Operations\assets\subPlot13.jpg" alt="Image 3" width="1600"></td>
    </tr>
    <tr>
        <td>Grayscale</td>
        <td>Negative</td>
        <td>Brighten</td>
    </tr>
    <tr>
        <td><img src="./Point Operations\assets\subPlot21.jpg" alt="Image 4" width="1600"></td>
        <td><img src="./Point Operations\assets\subPlot22.jpg" alt="Image 5" width="1600"></td>
        <td><img src="./Point Operations\assets\subPlot23.jpg" alt="Image 6" width="1600"></td>
    </tr>
    <tr>
        <td>Low Contrast</td>
        <td>4 BPP</td>
        <td>Flip</td>
    </tr>
</table>


## Linear Filters

 Predefined filters are applied to a grayscale image. The goal of this lab is to use custom filters to perform various image processing tasks such as edge detection, blurring, and sharpening.

### Exercise Description

In this lab, you are required to:

1. **Load a color image** (in JPG or PNG format) from the disk and convert it to an 8-bpp grayscale format.
2. **Apply four different filters** to the grayscale image. The filters are provided as numpy arrays.
3. **Save the filtered images** to disk with appropriate filenames.

### Provided Filters

The following filters are provided as 5x5 numpy arrays:

1. **Filter 1 (Filter A) - Laplacian of Gaussian (LoG) Filter:**
    ```python
    filter1 = normalize_filter(np.array([
        [0, -1, -1, -1, 0],
        [-1, 2, 2, 2, -1],
        [-1, 2, 8, 2, -1],
        [-1, 2, 2, 2, -1],
        [0, -1, -1, -1, 0]
    ]))
    ```

2. **Filter 2 (Filter B) - Gaussian Blur Filter:**
    ```python
    filter2 = normalize_filter(np.array([
        [1, 4, 6, 4, 1],
        [4, 16, 24, 16, 4],
        [6, 24, 36, 24, 6],
        [4, 16, 24, 16, 4],
        [1, 4, 6, 4, 1]
    ]))
    ```

3. **Filter 3 (Filter C) - Uniform Box Filter:**
    ```python
    filter3 = normalize_filter(np.array([
        [5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5]
    ]))
    ```

4. **Filter 4 (Filter D) - Sharpening Filter (High-Boost Filter):**
    ```python
    filter4 = normalize_filter(np.array([
        [0, -1, -1, -1, 0],
        [-1, 2, 2, 2, -1],
        [-1, 2, 16, 2, -1],
        [-1, 2, 2, 2, -1],
        [0, -1, -1, -1, 0]
    ]))
    ```

## Requirements

- OpenCV (for loading the source image and saving the output images)
- Numpy

## Installation

To run the script, you need to install the required libraries. You can install them using `pip`:

```bash
pip install numpy opencv-python
```

Usage
Place your source image (in JPG or PNG format) in the repository directory.

Edit the script specifying the path to your image.
```python
img = cv.imread('{path-to-your-image}')
```
*   If you are running the python script, make sure to cd in to the `/Point Operations` or change the image path accordingly. Otherwise the script will fail with `Error: Image not found.` message.

Run the apply_filters.py script using Python:


The script will apply each filter to the grayscale image and save the resulting images to disk with filenames indicating the filter used.

<table>
    <tr>
        <td><img src="./Linear Filters/road98.png" alt="Image 1" width="1600"></td>
        <td><img src="./Linear Filters/original.jpg" alt="Image 2" width="1600"></td>
    </tr>
    <tr>
        <td>Input Image</td>
        <td>Grayscale (Original)</td>
    </tr>
     <tr>
        <td><img src="./Linear Filters/filterA.jpg" alt="Image 1" width="1600"></td>
        <td><img src="./Linear Filters/filterB.jpg" alt="Image 2" width="1600"></td>
    </tr>
    <tr>
        <td>LoG Filter</td>
        <td>Gaussian Blue Filter</td>
    </tr>
    <tr>
        <td><img src="./Linear Filters/filterC.jpg" alt="Image 3" width="1600"></td>
        <td><img src="./Linear Filters/filterD.jpg" alt="Image 4" width="1600"></td>
    </tr>
    <tr>
        <td>Uniform Box Filter</td>
        <td>Hight Boost Filter</td>
    </tr>
</table>
