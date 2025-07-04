import cv2
import numpy as np

def pastel_effect(image_path, output_path='pastel_output.jpg'):
    # Load image
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Step 1: Bilateral Filter for soft color transitions
    pastel = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

    # Step 2: Slight color boost
    pastel = cv2.convertScaleAbs(pastel, alpha=1.1, beta=10)

    # Step 3: Light Gaussian Blur
    pastel = cv2.GaussianBlur(pastel, (5, 5), 0)

    # Step 4: Add slight noise for pastel texture
    noise = np.random.normal(0, 10, pastel.shape).astype(np.uint8)
    pastel = cv2.add(pastel, noise)

    # Step 5: Save or show
    pastel_bgr = cv2.cvtColor(pastel, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, pastel_bgr)

    return pastel

# Example usage:
pastel_image = pastel_effect("girl.jpg")
import matplotlib.pyplot as plt

def show_image(img):
    plt.imshow(img)
    plt.axis('off')
    plt.show()

# After pastel_effect returns
show_image(pastel_image)
