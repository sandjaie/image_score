"""
Program to calulate the similarity score between set of images

Returns:
    output_file with score and execution time
"""

import os
import timeit
import csv
# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity as compare_ssim
from PIL import Image
import cv2


def find_image_score(img_a, img_b, height, width):
    """
    Calculates the image similarity score and execution time

    Arguments:
        img_a {[image]} -- [image1 from the input file].
        img_b {[image]} -- [image2 from the input file].

    Returns:
        score           -- Score of the similarity between the images compared.
        execution_time  -- Time in secs it takes to run the score for each set of images.
    """
    try:
        start = timeit.default_timer()
        print(f"height: {height} Width: {width}")
        std_dimensions = (height, width)
        img_a_resized = cv2.resize(cv2.imread(img_a), std_dimensions)
        img_b_resized = cv2.resize(cv2.imread(img_b), std_dimensions)

        ssim, _ = compare_ssim(img_a_resized, img_b_resized, full=True, multichannel=True)
        score = round(1 - ssim, 2)

        stop = timeit.default_timer()
        execution_time = round(stop - start, 2)
        return [score, execution_time]

    except Exception as err:
        return f"find_image_score:{err}"


def write_output(infile, outfile, height, width):
    """Writes the output file 'output.csv'
    """
    with open(outfile, 'w') as out_file:
        with open(infile, 'r') as in_file:
            csv_reader = csv.reader(in_file, delimiter=',')
            next(csv_reader)
            out_file_headers = "image1,image2,similar,elapsed"
            out_file.write(out_file_headers + '\n')

            for row in csv_reader:
                image_score = find_image_score(row[0], row[1], height, width)
                print("Score: ", image_score)
                out_file.write(",".join(map(str, row)))
                out_file.write(',' + ','.join(map(str, image_score)) + '\n')
                print(f"Comparison of {row[0]} and {row[1]} is completed\n")
    if os.path.exists(outfile):
        return outfile


def check_file(infile):
    """Checks if the file is empty
    """
    with open(infile, 'r') as input_file:
        if input_file.readline() == '':
            return f"{infile} is empty"


def check_images_in_file(infile):
    """
    Checks the input file

    checks the file contents are actual images,
    checks the images are present in the path

    Returns:
        None -- [returns None if the checks succeeds else returns the error]
    """
    with open(infile, 'r') as input_file:
        reader = csv.reader(input_file, delimiter=',')
        next(reader)
        for row in reader:
            try:
                Image.open(row[0])
                Image.open(row[1])
            except Exception as err:
                return f"check_image: {err}"


def main(infile, outfile, height, width):
    """
    Main function

    checks if the input file exists and if
    check_image is successful, calls the write_output
    """
    if os.path.exists(infile):
        if check_file(infile) and check_images_in_file(infile) is None:
            write_output(infile, outfile, height, width)
    else:
        return f"Input file: {infile} is missing"
