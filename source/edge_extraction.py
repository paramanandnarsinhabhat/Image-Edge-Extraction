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

#plotting the sobel horizontal edges
imshow(edges_sobel_horizontal,cmap='gray')

plt.show()


#plotting the sobel vertical edges
imshow(edges_sobel_vertical,cmap='gray')

plt.show()

## Prewitt Kernel
#calculating horizontal edges using prewitt kernel
edges_prewitt_horizontal = prewitt_h(image)

#calculating vertical edges using prewitt kernel
edges_prewitt_vertical = prewitt_v(image)

#plotting prewitt horizontal edges
imshow(edges_prewitt_horizontal,cmap='gray')


plt.show()