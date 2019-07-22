from skimage.measure import compare_ssim
from PIL import Image
import cv2
from score.findscore import find_image_score, check_file, check_images_in_file, main, write_output
from tests.test_config import *

# image1 = 'tests/images/ac.png'
# image2 = 'tests/images/bc.png'
# image3 = 'tests/images/bb.jpg'
# height = 512
# width = 512
# infile = 'tests/test_input.csv'
# outfile = 'tests/test_output.csv'


def cal_score(img_a, img_b):
    ssim, _ = compare_ssim(img_a, img_b, full=True, multichannel=True)
    score = round(1 - ssim, 2)
    return score

def test_find_image_score_1():
    img_a = cv2.resize(cv2.imread(image1), (height, width))
    img_b = cv2.resize(cv2.imread(image2), (height, width))
    score = cal_score(img_a, img_b)
    assert score == 0.0

def test_find_image_score_2():
    img_a = cv2.resize(cv2.imread(image1), (height, width))
    img_b = cv2.resize(cv2.imread(image3), (height, width))
    score = cal_score(img_a, img_b)
    assert score == 0.66

def test_check_image_1():
    img = Image.open(image1)
    assert img.size == (550, 541)

def test_check_file():
    assert check_file(infile) == 'OK'

def test_find_image_score():
    score1, _ = find_image_score(image1, image2, height, width)
    score2, _ = find_image_score(image1, image3, height, width)
    assert score1 == [0.0]
    assert score2 == [0.66]

def test_check_images_in_file():
    assert check_images_in_file(infile) == 'OK'

def test_main():
    assert main(infile, outfile, height, width) == 'OK'

def test_write_output():
    assert write_output(infile, outfile, height, width) == 'OK'
