import cv2
import color_descriptor
import searcher
import montage
import os
import test_caption

#stored features file of out database
index_path = "src/index.csv"

#query image
input = input("Just enter the image file name: ")
query_image_path = "src/queries/" + input

#database with which results will be shown
database_path = "src/dataset/"

# number of bins for color descriptor (H, S, V) respectively
# total bins = 8*12*3 = 288
bins = (8, 12, 3)

def Search(index_path, query_image_path, database_path, bins):
    # loading query image
    query_image = cv2.imread(query_image_path)

    # features list of query image as per the 5 regions
    query_features = color_descriptor.feature_extractor(query_image, bins)
    # print(len(query_features))

    # searching the database for similar images and getting the results
    search_results = searcher.Search(index_path, query_features)
    # print(search_results)

    results_image_paths = []
    for (score, resultID) in search_results:
        results_image_paths.append("src/dataset/" + resultID)

    montages = montage.build_montage(results_image_paths)

    # loop over the montages and display each of them
    for m in montages:
        cv2.imshow("Montage", m)
        cv2.waitKey(0)
    
    # storing the output in output folder in src
    cv2.imwrite("src/output/montage_"+ os.path.splitext(input)[0] +".png", m)

if __name__ == "__main__":
    # Search(index_path, query_image_path, database_path, bins)
    caption = test_caption.returns_caption(query_image_path)

    print("############################################################################################")
    print(caption)
    print("############################################################################################")

    