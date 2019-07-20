import csv
import cv2
import timeit
from skimage.measure import compare_ssim
from config import *

def score(img_a, img_b):
    start = timeit.default_timer()
    std_dimensions = (LENGTH, BREADTH)
    img_a = cv2.imread(img_a)
    img_b = cv2.imread(img_b)

    img_a_resized = cv2.resize(img_a, std_dimensions)
    img_b_resized = cv2.resize(img_b, std_dimensions)

    # score: {-1:1} measure of the structural similarity between the images
    ssim, diff = compare_ssim(img_a_resized, img_b_resized, full=True, multichannel=True)
    score = round(1 - ssim, 2)
    stop = timeit.default_timer()
    
    execution_time = round(stop - start, 2)
    #print(f"Start: {start} Stop: {stop} Elapsed: {execution_time}")
    return [score, execution_time]


def main():
    with open('output.csv', 'w') as outfile:
        with open('input.csv', 'r') as infile:
            csv_reader = csv.reader(infile, delimiter=',')
            skip_header = next(csv_reader)
            outfile_headers = "image1,image2,similar,elapsed"
            outfile.write(outfile_headers + '\n')
            for row in csv_reader:
                image_score = score(row[0], row[1])
                outfile.write(",".join(map(str,row)))
                outfile.write(',' + ','.join(map(str, image_score)) + '\n')
                print(f"Comparison of {row[0]} and {row[1]} is completed\n")

if __name__ == "__main__":
    main()