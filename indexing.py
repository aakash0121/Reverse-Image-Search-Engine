import cv2
import glob
import color_descriptor
from test import bins

output = open("src/index.csv", 'w')

for imagePath in glob.glob("src/dataset" + "/*.png"):
	# extract the image ID from the image path and load that image
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)

	# describe the image
	features = color_descriptor.feature_extractor(image, bins)

	# write the features to file
	features = [str(f) for f in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))

# close the index file
output.close()