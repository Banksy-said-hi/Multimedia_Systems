import os
import numpy as np
from PIL import Image

def mse(imageA, imageB):
    # Calculate the Mean Squared Error between two images
    err = np.sum((np.array(imageA).astype("float") - np.array(imageB).astype("float")) ** 2)
    err /= float(imageA.size[0] * imageA.size[1])
    return err

def psnr(original, compressed):
    # Calculate PSNR (Peak Signal-to-Noise Ratio)
    mse_value = mse(original, compressed)
    if mse_value == 0:  # Means no difference
        return float('inf')
    max_pixel = 255.0
    return 20 * np.log10(max_pixel / np.sqrt(mse_value))

# Path to your original PNG image
image_path = 'garnacho.png'

# Load the original image
original_image = Image.open(image_path)

# Print original image details
print(f"The original image {image_path} has been loaded.")
print(f"Original image size: {original_image.size}")
print(f"Original image mode: {original_image.mode}")
print("===========================================")

# Define the compression level for compression
compression_level = int(input("Enter compression quality (1-95): "))
print("Thanks for entering the number :)")
print("===========================================")
print(f"Compression level set to {compression_level}")
print("===========================================")

# If the image is in RGBA mode, convert it to RGB before compression
if original_image.mode == 'RGBA':
    rgb_original_image = original_image.convert('RGB')
else:
    rgb_original_image = original_image

# Specify the filename for the compressed image
compressed_image_path = 'compressed_garnacho.jpg'

# Compress and save the image as JPEG
rgb_original_image.save(compressed_image_path, 'JPEG', quality=compression_level)
print(f"Image has been compressed and saved as {compressed_image_path}")

# Get the file sizes of the original and compressed images
original_size = os.path.getsize(image_path)
compressed_size = os.path.getsize(compressed_image_path)

# Print file size information
print(f"Original image size: {original_size} bytes")
print(f"Compressed image size: {compressed_size} bytes")
print("Calculating the size difference...")
# Calculate and print the size reduction
size_difference = original_size - compressed_size

print("===========================================")
print(f"Size reduction: {size_difference} bytes")
print("===========================================")

# Load the compressed JPEG image
compressed_image = Image.open(compressed_image_path)

# Specify the filename for the decompressed image (back to PNG format)
decompressed_image_path = 'decompressed_garnacho.png'

# Save the decompressed image as PNG
compressed_image.save(decompressed_image_path, 'PNG')
print(f"Compressed image has been reconstructed back to PNG format as {decompressed_image_path}")

# Optionally, you can compare the size of this new PNG with the original PNG
decompressed_size = os.path.getsize(decompressed_image_path)

print("===========================================")
print(f"Original image size: {original_size} bytes")
print(f"Compressed image size: {compressed_size} bytes")
print(f"Decompressed image size: {decompressed_size} bytes")
print("===========================================")

# Calculate PSNR
print("Calculating the PSNR...")
psnr_value = psnr(rgb_original_image, compressed_image)
print("===========================================")
print(f"PSNR value: {psnr_value} dB")
print("===========================================")
