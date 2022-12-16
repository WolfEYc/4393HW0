import math

import numpy as np
import cv2


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


class Operation:

    def __init__(self):
        pass

    def merge(self, image_left, image_right, column):
        """
        Merge image_left and image_right at column (column)
        
        image_left: the input image 1
        image_right: the input image 2
        column: column at which the images should be merged

        returns the merged image at column
        """

        merged = image_left.copy()
        merged[:, column:] = image_right[:, column:]

        # same as below but just longer, ultimatley performes the same operation without much syntactical difference
        # np.concatenate((image_left[:, :column], image_right[:, column:]), axis=1)
        return merged

    def intensity_scaling(self, input_image, column, alpha, beta):
        """
        Scale your image intensity.

        input_image: the input image
        column: image column at which left section ends
        alpha: left half scaling constant
        beta: right half scaling constant

        return: output_image
        """

        # add your code here
        input_image = input_image.copy()

        input_image[:, :column] = np.uint8(input_image[:, :column] * alpha)
        input_image[:, column:] = np.uint8(input_image[:, column:] * beta)

        # Please do not change the structure
        return input_image  # Currently the input image is returned, please replace this with the intensity scaled image

    def centralize_pixel(self, input_image, column):
        """
        Centralize your pixels (do not use np.mean)

        input_image: the input image
        column: image column at which left section ends

        return: output_image
        """

        mL = np.sum(input_image[:, :column]) / (len(input_image) * column)
        mR = np.sum(input_image[:, column:]) / (len(input_image) * column)

        print(f'ML: {mL} MR: {mR}')

        oL = 128 - mL
        oR = 128 - mR

        print(f'OL: {oL} OR: {oR}')

        input_image = input_image.copy()

        # same as np.clip just less efficient bc run in python
        for r in range(len(input_image)):
            for c in range(column):
                input_image[r, c] = clamp(input_image[r, c] + oL, 0, 255)

        for r in range(len(input_image)):
            for c in range(column, len(input_image[r])):
                input_image[r, c] = clamp(input_image[r, c] + oR, 0, 255)

        # same as this but just slower,
        # doesnt make much sense as the point of python
        # is to use these fast C libraries rather than slow python interpreted code

        # input_image[:, :column] = np.clip(input_image[:, :column] + oL, 0, 255)
        # input_image[:, column:] = np.clip(input_image[:, column:] + oR, 0, 255)

        return input_image
