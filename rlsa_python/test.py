import cv2
import os

from rlsa_python.rlsa import RLSA

def binary_invert(img):
        """
        Method that converts the image to inverse binary.

        Parameters:
            img (numpy.array): The page image to be inverted.

        Returns:
            numpy.array: Binary invrted image.
        """

        gray_scale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        __, binary_image = cv2.threshold(gray_scale, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        return binary_image


if __name__ == "__main__":
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(ROOT_PATH, "test_data", "text_image.png")

    img = cv2.imread(image_path)
    inverted_image = binary_invert(img)
    smeared_image = RLSA.apply_rlsa(inverted_image, 80, 100, 10)

    cv2.imwrite(os.path.join(ROOT_PATH, "test_data", "text_image_result.png"), smeared_image)
    

