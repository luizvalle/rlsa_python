# -*- coding: utf-8 -*-
import itertools

import numpy as np


class RLSA(object):
    """
    Class that contains the logic to apply the Run Length Smoothing Algorithm (RLSA) on an image.
    """

    @staticmethod
    def apply_rlsa(img, h_threshold=0, v_threshold=0, hf_threshold=0):
        """
        Method that applies the 'smear_line' algorithm first to every row, then to every column, combines these two
        results with the logical 'and' (so that only the white pixels on both images remain), and applies 'smear_line'
        horizontally again to the combined result.

        Parameters:
            img (numpy.array): Array representing the image (must be binary image with only 0s or 255s. 255 pixels will be smeared).
            h_threshold (int): First threshold to be used horizontally.
            v_threshold (int): Threshold to be used vertically.
            hf_threshold (int): Final threshold value to be used horizontally.

        Returns:
            numpy.array: Array after application of RLSA.
        """

        horizontal_smear = np.apply_along_axis(RLSA.__smear_line, 1, img, h_threshold)
        vertical_smear = np.apply_along_axis(RLSA.__smear_line, 0, img, v_threshold)

        combined_smear = horizontal_smear & vertical_smear

        return np.apply_along_axis(RLSA.__smear_line, 1, combined_smear, hf_threshold).astype("uint8")

    @staticmethod
    def __rle_encode(line):
        """
        Method that encodes the given line using the Run Length Encoding algorithm.

        Parameters:
            line (numpy.array): The line to be encoded.

        Returns:
            numpy.array: An array of tuples representing the encoded line in the form (value, frequency).
        """

        return [(pixel_value, len(list(group))) for pixel_value, group in itertools.groupby(line)]

    @staticmethod
    def __join_lines(line1, line2):
        """
        Method that joins two lines

        Parameters:
            line1 (numpy.array): 1D array.
            line2 (numpy.array): 1D array.

        Returns:
            numpy.array: line1 appended to the beginning of line2.
        """

        line2[0:0] = line1
        return line2

    @staticmethod
    def __smear_line(line, threshold):
        """
        Method that 'smears' the given line. 0's are changed into 255's in the final array
        if the nummber of consecutive 0's is less than or equal to (<=) the given 'threshold'.
        255's remain unchanged in the final array.

        Parameters:
            line (numpy.array): Binary 1D array of either 0 or 255.
            threshold (int): Threshold value used for the algorithm described above.

        Returns:
            numpy.array: Smeared line.
        """

        encoded_line = RLSA.__rle_encode(line)

        smeared_line = list()
        for group in encoded_line:
            pixel_value, frequency = group
            if pixel_value == 0 and frequency > threshold:
                smeared_line = RLSA.__join_lines(smeared_line, [0] * frequency)
            else:
                smeared_line = RLSA.__join_lines(smeared_line, [255] * frequency)
        return smeared_line

