from PIL import Image
Image.open("")

img  = Image.open("")
# File format of the src
print("Format: " + img.format)   # Output: JPEG

# Pixel format used by src
# Typical values are "2", "L", "RGB", "CNYK."
print("Pixel format: " + img.mode)  # Output: RGB

# Src size in pixels
print("Size: " + img.size)  # Output: (x, y)

print(img.palette)
