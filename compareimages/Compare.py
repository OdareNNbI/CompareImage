from skimage import measure
import glob
import math
import os
from PIL import Image
import skimage.measure
import cv2
import numpy

def compute_psnr(img1, img2): #- разница в шуме в дцбелах? 0 - similar
    return cv2.PSNR(img1, img2)

def mse(imageA, imageB): # - 0 сходство - проверяет интенсивность пикселей
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = numpy.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

#SSIM - -1 до 1, 1-индеалное сходство, работает по окнам, а не по всему излоюражению

myImagePostfix = "_ne4x"
pMyDirectory = "PResult/"
pVanyaDirectory = "PVanya/"


vMyDirectory = "VResult/"
vVanyaDirectory = "VVanya/"

pSize = 773
vSize = 563

mediumPsnr = 0
mediumMse = 0
mediumSsim = 0
for i in range(pSize):
    imageNumber = i + 1
    myFilename = pMyDirectory + str(imageNumber) + myImagePostfix + ".jpg"
    vanyaFilename = pVanyaDirectory + str(imageNumber) + ".jpg"
    first = cv2.imread(myFilename)
 #   first = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
    second = cv2.imread(vanyaFilename)
  #  second = cv2.cvtColor(second, cv2.COLOR_BGR2GRAY)
    mediumPsnr += compute_psnr(first, second)
    mediumMse += mse(first, second)
    mediumSsim += measure._structural_similarity.structural_similarity(first, second, multichannel=True)

print("P folder psnr - " + str(mediumPsnr / pSize))
print("P folder mse - " + str(mediumMse / pSize))
print("P folder ssim - " + str(mediumSsim / pSize))

mediumPsnr = 0
mediumMse = 0
mediumSsim = 0
for i in range(vSize):
    imageNumber = i + 1
    myFilename = vMyDirectory + str(imageNumber) + myImagePostfix + ".jpg"
    vanyaFilename = vVanyaDirectory + str(imageNumber) + ".jpg"
    first = cv2.imread(myFilename)
  #  first = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
    second = cv2.imread(vanyaFilename)
  #  second = cv2.cvtColor(second, cv2.COLOR_BGR2GRAY)
    mediumMse += mse(first, second)
    mediumPsnr += compute_psnr(first, second)
    mediumSsim += measure._structural_similarity.structural_similarity(first, second, multichannel=True)

print("V folder psnr - " + str(mediumPsnr / vSize))
print("V folder mse - " + str(mediumMse / vSize))
print("V folder ssim - " + str(mediumSsim / vSize))