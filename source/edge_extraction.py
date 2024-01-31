#Load Required libraries and images
#Import the required libraries
from skimage.io import imread, imshow
from skimage.filters import sobel_h,prewitt_h,prewitt_v,sobel_v
import matplotlib.pyplot as plt
#reading the image and plotting it
image = imread('/Users/paramanandbhat/Downloads/Extracting Edges/dog.jpg', as_gray=True)
imshow(image,cmap='gray')

plt.show()

print(image.shape)

## Sobel Kernel

#calculating the horizontal edges using sobel kernel
edges_sobel_horizontal = sobel_h(image)

#calculating the vertical edges using soble kernel
edges_sobel_vertical = sobel_v(image)


print(edges_sobel_horizontal)

print(edges_sobel_vertical)

