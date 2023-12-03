from PIL import Image

def convert_to_png(image_path, output_path, size=(24, 24)):
    # Open an image file
    img = Image.open(image_path)
    # Resize it to the desired size
    img = img.resize(size, Image.LANCZOS)
    # Save it as a new file in .png format
    img.save(output_path, "PNG")

convert_to_png("/home/m/MeDott29.github.io/new.jpg", "/home/m/MeDott29.github.io/new.png")