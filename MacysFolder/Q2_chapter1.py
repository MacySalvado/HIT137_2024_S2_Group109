import time
from PIL import Image
import os


# Generate the number using the provided code
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10

print(f"Generated Number: {generated_number}")

# Open the provided image
image_path = "chapter1.jpg"
try:
    image = Image.open(image_path)
    pixels = image.load()

    # Create a new image with altered pixels
    new_image = Image.new("RGB", image.size)
    new_pixels = new_image.load()

    # Alter the pixel values
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            new_r = min(r + generated_number, 255)
            new_g = min(g + generated_number, 255)
            new_b = min(b + generated_number, 255)
            new_pixels[i, j] = (new_r, new_g, new_b)

    # Save the new image
    new_image_path = "chapter1out.png"
    new_image.save(new_image_path)

    # Calculate the sum of all red pixel values in the new image
    red_sum = sum(new_pixels[i, j][0] for i in range(new_image.width) for j in range(new_image.height))

    print(f"Sum of all red pixel values: {red_sum}")

except FileNotFoundError:
    print("The file 'chapter1.jpg' was not found. Please make sure the file is in the correct directory.")


# please see the "chapter1out.png" we created after running the code at 10:26 PM
# yay, it works! :)