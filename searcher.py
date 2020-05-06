import csv
import numpy as np 

def chi2_distance(histA, histB, eps = 1e-10):
    # compute the chi-squared distance
    d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(histA, histB)])
    return d

def Search(index_path, query_features, limit = 10):
    # results dictionary
    results = {}
    
    # open the index csv file
    with open(index_path) as f:
        reader = csv.reader(f)
        # loop over all the image feature entries in the index.csv
        for entry in reader:
            # getting Image ID and features and computing distance using chi-square
            # distance between the query_features and features of images in database
            features = [float(x) for x in entry[1:]]
            d = chi2_distance(features, query_features)

            # storing distance calculated above into results dictionary
            results[entry[0]] = d
        
        f.close()

    # sort the results dictionary with values(distance) of Image IDs(keys)
    results = sorted([(v, k) for (k, v) in results.items()])
    return results[:limit]
    