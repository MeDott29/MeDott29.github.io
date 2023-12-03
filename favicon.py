from PIL import Image

def create_favicon(image_path, favicon_path, size=(32, 32)):
    # Open an image file
    img = Image.open(image_path)
    # Get dimensions
    width, height = img.size
    # Determine the area to crop
    left = width/4
    top = height/4
    right = 3 * width/4
    bottom = 3 * height/4
    # Crop the center of the image
    img = img.crop((left, top, right, bottom))
    # Resize it to the desired size
    img = img.resize(size, Image.LANCZOS)
    # Save it as a new file in .ico format
    img.save(favicon_path, "ICO")

create_favicon("/home/m/MeDott29.github.io/new.jpg", "/home/m/MeDott29.github.io/docs/img/favicon.ico")