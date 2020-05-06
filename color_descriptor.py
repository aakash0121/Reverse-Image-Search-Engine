import numpy as np
import cv2
import imutils

def histogram(image, bins, mask):
		
		hist = cv2.calcHist([image], [0, 1, 2], mask, bins, [0, 180, 0, 256, 0, 256])
			
		if imutils.is_cv2():
			hist = cv2.normalize(hist).flatten()
		else:
			hist = cv2.normalize(hist, hist).flatten()

		return hist

def color_descriptor(image, bins):
    features = []
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	
    (h, w) = image.shape[:2]
    (cX, cY) = (int(w * 0.5), int(h * 0.5))
    
    segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h), (0, cX, cY, h)]

    (axesX, axesY) = (int(w * 0.75) // 2, int(h * 0.75) // 2)
    ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
    cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)

    for (startX, endX, startY, endY) in segments:
        cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
        cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
        cornerMask = cv2.subtract(cornerMask, ellipMask)
        hist = histogram(image, bins, cornerMask)
        features.extend(hist)

    hist = histogram(image, ellipMask)
    features.extend(hist)
    return features
