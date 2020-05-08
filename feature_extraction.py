from pickle import dump
from PIL import Image
from keras.applications.xception import Xception, preprocess_input
import numpy as np 
import os
from tqdm import tqdm_notebook as tqdm
tqdm().pandas()

def extract_features(directory):
    model = Xception( include_top=False, pooling='avg' )
    features = {}
    for img in tqdm(os.listdir(directory)):
        filename = directory + "/" + img
        image = Image.open(filename)
        image = image.resize((299,299))
        image = np.expand_dims(image, axis=0)
        #image = preprocess_input(image)
        image = image/127.5
        image = image - 1.0
        feature = model.predict(image)
        features[img] = feature
    return features

#2048 feature vector
dataset_images = "src/flickr8k/Images"
features = extract_features(dataset_images)
dump(features, open("src/features.p","wb"))