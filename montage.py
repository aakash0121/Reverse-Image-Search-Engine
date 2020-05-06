from imutils import build_montages
from imutils import paths
import cv2

def build_montage(results_image_paths):
    # initialize the list of images
    images = []
    # loop over the list of image paths
    for imagePath in results_image_paths:
        # load the image and update the list of images
        image = cv2.imread(imagePath)
        images.append(image)
    # construct the montages for the images
    montages = build_montages(images, (400, 400), (5, 2))

    # loop over the montages and display each of them
    for montage in montages:
        cv2.imshow("Montage", montage)
        cv2.waitKey(0)

