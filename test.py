import cv2
import color_descriptor
import searcher

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
query_features = color_descriptor.feature_extractor(query_image)

# searching the database for similar images and getting the results
search_results = searcher.Search(index_path, query_features)
