import cv2
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Attempt to load the image
image = cv2.imread('batman.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
y, u, v = cv2.split(yuv_image)

# Print the original image
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')
plt.show()
print("=========================================================================")

# Print the Y layer
plt.imshow(y, cmap='gray')
plt.title('Y (Luminance) Channel')
plt.axis('off')
plt.show()
print("=========================================================================")

# Apply DCT to the Y channel and print the DCT coefficients matrix
dct_y = cv2.dct(np.float32(y))
print(tabulate(dct_y, tablefmt="plain", floatfmt=".2f"))
print("=========================================================================")

# Set the bottom-right 3x3 coefficients to zero and print the matrix
dct_y[-3:, -3:] = 0
print(tabulate(dct_y, tablefmt="plain", floatfmt=".2f"))
print("=========================================================================")

# Revert the process: Apply inverse DCT to get the new Y channel
idct_y = cv2.idct(dct_y)
# Clamp the values to the range 0-255 to avoid wrapping around
idct_y = np.clip(idct_y, 0, 255)

# Merge the new Y channel with the U and V channels
yuv_processed = cv2.merge([np.uint8(idct_y), u, v])

# Convert the processed YUV image back to RGB
rgb_processed = cv2.cvtColor(yuv_processed, cv2.COLOR_YUV2RGB)

# Generate the new image and print it alongside the original image
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(image_rgb)
axs[0].set_title("Original Image")
axs[0].axis('off')

axs[1].imshow(rgb_processed)
axs[1].set_title("Modified Image")
axs[1].axis('off')

plt.show()
