from PIL import Image
import time

# Function to change pixel values based on the generated number
def change_pixel_color(pixel, generated_number):
    r, g, b = pixel
    new_r = (r + generated_number) % 256
    new_g = (g + generated_number) % 256
    new_b = (b + generated_number) % 256
    return new_r, new_g, new_b

# Open the original image
original_image_path = "D:\Shem\chapter1.jpg"
original_image = Image.open(original_image_path)

# Create the number as described in the story
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10

# Analyze every pixel in the image
new_image = Image.new('RGB', original_image.size)
for y in range(original_image.height):
    for x in range(original_image.width):
        pixel = original_image.getpixel((x, y))
        new_pixel = change_pixel_color(pixel, generated_number)
        new_image.putpixel((x, y), new_pixel)

# Save new image
new_image_path = 'chapter1_out.png'
new_image.save(new_image_path)

# Calculate sum of red (r) pixel values in the new image
red_pixel_sum = sum(new_pixel[0] for new_pixel in new_image.getdata())

# Output the sum for the next chapter
print("Sum of red pixel values in the new image:", red_pixel_sum)

