import csv
import cv2
from skimage.measure import compare_ssim

def cal_score(img_a, img_b):
    ssim, _ = compare_ssim(img_a, img_b, full=True, multichannel=True)
    score = round(1 - ssim, 2)
    return score

def test_find_score_1():
    img_a = cv2.resize(cv2.imread('tests/images/ac.png'), (512,512))
    img_b = cv2.resize(cv2.imread('tests/images/bc.png'), (512,512))
    score = cal_score(img_a, img_b)
    assert score == 0.0

def test_find_score_2():
    img_a = cv2.resize(cv2.imread('tests/images/ac.png'), (512,512))
    img_b = cv2.resize(cv2.imread('tests/images/bb.jpg'), (512,512))
    score = cal_score(img_a, img_b)
    assert score == 0.66
