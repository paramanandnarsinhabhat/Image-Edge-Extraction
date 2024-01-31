#Load Required libraries and images
#Import the required libraries
from skimage.io import imread, imshow
from skimage.filters import sobel_h,prewitt_h,prewitt_v,sobel_v

#reading the image and plotting it
image = imread('/Users/paramanandbhat/Downloads/Extracting Edges/dog.jpg', as_gray=True)
imshow(image,cmap='gray')