import cv2
import streamlit as st
# Load image
img = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
img = cv2.imread('your_image.jpg')

# Apply bilateral filter (smooth color while preserving edges)
for i in range(2):
    image = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply median blur
gray = cv2.medianBlur(gray, 7)

# Detect edges using adaptive threshold
edges = cv2.adaptiveThreshold(gray, 255, 
                               cv2.ADAPTIVE_THRESH_MEAN_C, 
                               cv2.THRESH_BINARY, 9, 2)

# Convert back to color
edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# Combine edges with the original (smoothed) image
watercolor = cv2.bitwise_and(image, edges)

# Show result
cv2.imshow('Watercolor Effect', watercolor)
cv2.waitKey(0)
cv2.destroyAllWindows()
