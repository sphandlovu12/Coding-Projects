from PIL import Image

def Images_pdf(filename, output):
    images = []

    for file in filename:
        im = Image.open(file)
        im = im.convert('RGB')
        images.append(im)

        images[0].save(output, save_all=True, append_images[1:])

# Images Path, output pdf
Images_pdf([".png"], "output.pdf")