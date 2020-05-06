import cv2
import color_descriptor
import searcher
import montage

#stored features file of out database
index_path = "src/index.csv"

#query image
query_image_path = "src/queries/1.png"

#database with which results will be shown
database_path = "src/dataset/"

# number of bins for color descriptor (H, S, V) respectively
# total bins = 8*12*3 = 288
bins = (8, 12, 3)

# loading query image
query_image = cv2.imread(query_image_path)

# features list of query image as per the 5 regions
query_features = color_descriptor.feature_extractor(query_image, bins)
# print(len(query_features))

# searching the database for similar images and getting the results
search_results = searcher.Search(index_path, query_features)
# print(search_results)

# display the query
# cv2.imshow("Query", query_image)

# loop over the results
# for (score, resultID) in search_results:
# 	# load the result image and display it
# 	result = cv2.imread("src/dataset/" + resultID)
# 	cv2.imshow("Result", result)
# 	cv2.waitKey(0)

results_image_paths = []
for (score, resultID) in search_results:
    results_image_paths.append("src/dataset/" + resultID)

montage.build_montage(results_image_paths)