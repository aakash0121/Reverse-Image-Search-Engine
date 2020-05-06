import csv
import numpy as np 

def Search(index_path, query_features, limit = 10):
    # results dictionary
    results = {}
    
    # open the index csv file
    with open(index_path) as f:
        reader = csv.reader(f)

        