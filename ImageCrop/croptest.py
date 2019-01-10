import cv2
import numpy as np
from skimage.util import random_noise

def noisy(noise_typ,image):
    if noise_typ == "gauss":
        temp_img = np.float64(np.copy(image))
        row,col = temp_img.shape
        mean = 0
        var = 0.15
        sigma = var**0.5
        noise = np.random.normal(mean,sigma,(row, col))
        noisy_image = np.zeros(temp_img.shape, np.float64)
        if len(temp_img.shape) == 2:
            noisy_image = temp_img + noise
        else:
            noisy_image[:,:,0] = temp_img[:,:,0] + noise
            noisy_image[:,:,1] = temp_img[:,:,1] + noise
            noisy_image[:,:,2] = temp_img[:,:,2] + noise

        return noisy_image.astype(np.uint8)
    
    elif noise_typ == "s&p":
        row,col,ch = image.shape
        s_vs_p = 0.5
        amount = 0.004
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
        out[coords] = 1

        # Pepper mode
        num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
        out[coords] = 0
        return out
    elif noise_typ == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
        return noisy
    elif noise_typ =="speckle":
        row,col,ch = image.shape
        gauss = np.random.randn(row,col,ch)
        gauss = gauss.reshape(row,col,ch)        
        noisy = image + image * gauss
        return noisy

def scanlines(img, alpha):
    height, width = img.shape
    linewidth = 1
    step = int(height/60)
    overlay = img.copy()
    output = img.copy()
    for i in range(int(height/linewidth)):
        cv2.line(overlay, (0, i*step), (width, i*step), (0.4,0), linewidth)
    cv2.addWeighted(overlay, alpha, output, 1-alpha, 0, output)
    return output
        
def runimage(imagename, split):
    orig = cv2.imread(imagename, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
    noise = cv2.GaussianBlur(img, (5,5), 0)
    #img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
    #noise = noisy('gauss', noise)
    #noise1 = random_noise(img, mode='poisson', seed=None, clip=True)
    #noise2 = random_noise(noise, mode='localvar', seed=None, clip=True)
    newimg = scanlines(noise, alpha = 0.05)
    height, width = img.shape
    cut = width/split
    first = newimg[0:height, 0:int(width/split)]
    first = cv2.resize(first, (640,480))
    cv2.imwrite("first.jpg", first)
    second = newimg[0:height, int(width/split):int(2*width/split)]
    second = cv2.resize(second, (640,480))
    cv2.imwrite("second.jpg", second)
    third = newimg[0:height, int(2*width/split):int(3*width/split)]
    third = cv2.resize(third, (640,480)) 
    cv2.imwrite("third.jpg", third)
    fourth = newimg[0:height, int(3*width/split):int(4*width/split)]
    fourth = cv2.resize(fourth, (640,480)) 
    cv2.imwrite("fourth.jpg", fourth)

    #cv2.imshow("image1", noise1)
    #cv2.imshow("image", newimg)
    #cv2.imshow("normal", orig)
    cv2.imshow('one', first)
    cv2.imshow('two', second)
    cv2.imshow('three', third)
    cv2.imshow('four', fourth)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

runimage('test.jpg', 4)


