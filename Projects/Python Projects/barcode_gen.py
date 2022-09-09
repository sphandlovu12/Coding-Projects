import barcode
from barcode.writer import ImageWriter

# Define content of the barcode as a string
number = input("Enter the code to generate barcode: ")  #clcoding.com

# Get the required barcode format
barcode_format = barcode.get_barcode_class('upc')

# Generate barcode and render as image
my_barcode = barcode_format(number, writer=ImageWriter())

# Save barcode as PNG
my_barcode = barcode.save("generated_barcode")

from PIL import Image # to open the barcode and show
Image.open('generated_barcode.png') #clcoding