import cv2
import numpy as np 
from test import bins
import imutils


def histogram(image, mask):
    # extract a 3D color histogram from the masked region of the
    # image, using the supplied number of bins per channel
    hist = cv2.calcHist([image], [0, 1, 2], mask, bins,
        [0, 180, 0, 256, 0, 256])

    # normalize the histogram if we are using OpenCV 2.4
    if imutils.is_cv2():
        hist = cv2.normalize(hist).flatten()

    # otherwise handle for OpenCV 3+
    else:
        hist = cv2.normalize(hist, hist).flatten()
    return hist

def feature_extractor(query_image):
    # convert RGB color space into HSV
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # features list where we store all 5 regions feature
    features = []

    # dimensions of image
    h = image.shape[0]
    w = image.shape[1]

    # find out the center of the image
    (cx, cy) = (int(w*0.5), int(h*0.5))

    # divide the image into 5 regions
    # 1. top-left region
    top_left = (0, cx, 0, cy)
    # 2. top_right region
    top_right = (cx, w, 0, cy)
    # 3. bottom-left region
    bottom_left = (0, cx, cy, h)
    # 4. bottom-right region
    bottom_right = (cx, w, cy, h)
    # 5. middle elliptic region
    (aX, aY) = (int(w * 0.75) // 2, int(h * 0.75) // 2)
    ellipse_mask = np.zeros(image.shape[:2], dtype = "uint8")
    cv2.ellipse(ellipse_mask, (cx, cy), (aX, aY), 0, 0, 360, 255, -1)

    regions = (top_left, top_right, bottom_right, bottom_left)

    # loop over the first four segments
    for (sX, eX, sY, eY) in regions:
        # construct a mask for each corner of the image
        # subtracting the elliptical center from it
        side_mask = np.zeros(image.shape[:2], dtype = "uint8")
        cv2.rectangle(side_mask, (sX, sY), (eX, eY), 255, -1)
        siede_mask = cv2.subtract(side_mask, ellipse_mask)

        # extract a color histogram from the image, then update the features list
        hist = histogram(image, side_mask)
        features.extend(hist)
    
    # extract a color histogram from the elliptical region and update the feature vector
    hist = histogram(image, ellipse_mask)
    features.extend(hist)
    return features