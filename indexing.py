import cv2
import glob
import color_descriptor
import os

bins = (8, 12, 3)
output = open("src/index.csv", 'w')

for filename in os.listdir("src/dataset/"):
	print(filename)
	# extract the image ID from the image path and load that image
	imageID = filename[filename.rfind("/") + 1:]
	image = cv2.imread("src/dataset/"+filename)

	# describe the image
	features = color_descriptor.feature_extractor(image, bins)

	# write the features to file
	features = [str(f) for f in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))

# close the index file
output.close()