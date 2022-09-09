# The skimage package comes with data built-in that can run computer vision algorithms
from skimage import data, io, filters

image = data.coins()
edges = filters.sobel(image)
iio.imshow(edges)