from PIL import Image

# Open an image file
image = Image.open("1.jpeg")

# Save Image
image.save("result.jpeg")

# Crop Image
cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save("cropped.jpeg")

# Resize Image
resized_image = image.resize((200, 200))
resized_image.save("resized.jpeg")

# Filter Image
from PIL import ImageFilter
filtered_image = image.filter(ImageFilter.BLUR)
filtered_image.save("filtered.jpeg")


# Manipulasi Audio