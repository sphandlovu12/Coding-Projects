from PIL import Image

Image.open()    # original img

img = Image.open()
img2 = img.pygame.PixelArray.transpose(Image.FLIP_LEFT_RIGHT)
img2.save() # save as
Image.open()    # open mirror img
