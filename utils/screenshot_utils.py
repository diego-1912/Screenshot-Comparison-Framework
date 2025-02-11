import cv2
import numpy as np

def compare_images(baseline_path, new_path, diff_path, threshold=5.0):
    """
    Compare two images and save a diff image if differences are found.
    Uses a pixel intensity difference tolerance.
    """
    img1 = cv2.imread(baseline_path)
    img2 = cv2.imread(new_path)

    if img1 is None or img2 is None:
        raise FileNotFoundError(f"One of the images does not exist: {baseline_path} or {new_path}")

    # Resize new image to match baseline dimensions
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Compute absolute difference
    diff = cv2.absdiff(img1, img2)

    # Convert to grayscale for easier comparison
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Count number of different pixels (tolerance of 30 intensity levels)
    diff_percentage = (np.sum(gray_diff > 30) / gray_diff.size) * 100  

    if diff_percentage > threshold:
        print(f"UI Difference Detected: {diff_percentage:.2f}%")
        cv2.imwrite(diff_path, diff)  # Save the diff image for debugging
        return False  # Test fails
    return True  # Test passes
