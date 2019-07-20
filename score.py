"""
Program to calulate the similarity score between set of images

Returns:
    output_file with score and execution time
"""

import os
import timeit
import csv
import cv2
from skimage.measure import compare_ssim
from PIL import Image
import config as cfg


def find_score(img_a, img_b):
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
        std_dimensions = (cfg.width, cfg.height)
        img_a_resized = cv2.resize(cv2.imread(img_a), std_dimensions)
        img_b_resized = cv2.resize(cv2.imread(img_b), std_dimensions)

        ssim, _ = compare_ssim(img_a_resized, img_b_resized, full=True, multichannel=True)
        score = round(1 - ssim, 2)

        stop = timeit.default_timer()
        execution_time = round(stop - start, 2)
        return [score, execution_time]
    except Exception as err:
        print(err)


def write_output():
    """Writes the output file 'output.csv'
    """
    with open(cfg.output_file, 'w') as outfile:
        with open(cfg.input_file, 'r') as infile:
            csv_reader = csv.reader(infile, delimiter=',')
            next(csv_reader)
            outfile_headers = "image1,image2,similar,elapsed"
            outfile.write(outfile_headers + '\n')
            for row in csv_reader:
                image_score = find_score(row[0], row[1])
                outfile.write(",".join(map(str, row)))
                outfile.write(',' + ','.join(map(str, image_score)) + '\n')
                print(f"Comparison of {row[0]} and {row[1]} is completed\n")

def check_image():
    """
    Checks the input file

    checks the file contents are actual images,
    checks the images are present in the path

    Returns:
        None -- [returns None if the checks succeeds else returns the error]
    """
    with open(cfg.input_file, 'r') as infile:
        reader = csv.reader(infile, delimiter=',')
        next(reader)
        for row in reader:
            try:
                Image.open(row[0])
                Image.open(row[1])
            except Exception as err:
                return print(err)
    return None

def main():
    """
    Main function

    checks if the input file exists and if
    check_image is successful, calls the write_output
    """
    if os.path.exists(cfg.input_file):
        if check_image() is None:
            write_output()
    else:
        print(f"{cfg.input_file} file missing")

if __name__ == "__main__":
    main()
