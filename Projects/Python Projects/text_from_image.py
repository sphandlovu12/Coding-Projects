from PIL import Image
from pytesseract import pytesseract

# Define path to tesseract.exe
path_to_tesseract = 

# Define path to image
path_to_image = 

# Point tesseract_cmd to tesseract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# OPen image with PIL
img = Image.open(path_to_image)

# Extract text from image
text = pytesseract.image_to_string(img)
print(text)