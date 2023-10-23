import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image and convert color spaces
image = cv2.imread("spiderman.png")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
y, u, v = cv2.split(yuv_image)

# Binary thresholding
_, y_binary = cv2.threshold(y, 127, 255, cv2.THRESH_BINARY)

# 3-bit quantization (8 levels: 0, 32, 64, ..., 224)
y_3bit = np.floor_divide(y, 32) * 32 + 16
y_3bit[y_3bit > 255] = 255

# 4-bit quantization (16 levels: 0, 16, 32, ..., 240)
y_4bit = np.floor_divide(y, 16) * 16 + 8
y_4bit[y_4bit > 255] = 255

# Visualization

plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')
plt.show()

plt.imshow(y, cmap='gray')
plt.title('Y (Luminance) Channel')
plt.axis('off')
plt.show()

plt.imshow(y_binary, cmap='gray')
plt.title("1-Bit Y Channel")
plt.axis('off')
plt.show()

plt.imshow(y_3bit, cmap='gray')
plt.title("3-Bit Y Channel")
plt.axis('off')
plt.show()

plt.imshow(y_4bit, cmap='gray')
plt.title("4-Bit Y Channel")
plt.axis('off')
plt.show()
