# Reverse-Image-Search-Engine
Reverse Image Search Engine lets you search by an image as a query and returns you similar images plus original image with their respective tags.
It searches for best results on web as well as on its database and provides 10(or as per the user) images which it predicts most similar. It uses Image Captioning(for tagging) and different descriptors for identifying each image features.
When a user uploads an image it first tries to find tags and if it passes a certain confidence threshold if starts to search for similar images on the web while another search is going on within its database. Then, all the images which it finds suitable collects in one place and again passes to the descriptor for sequencing best 10 results and put it as a montage where an user can see the results.
And it is all wrapped up under the Flask environment to get a smooth experience of searching.

## Explanation
1. **color_descriptor.py**: It differentiates images on the basis of color density in 5 different regions of image and returns the 3D HSV color histogram.
2. **description_generator.py**: This script will create a file `src/descriptions.txt` which contains ImageID's with their captions.
3. **feature_extraction.py**: This script will create a pickle file `src/features.p` which contains all the `flickr8k dataset` images features for image tagging.
4. **image_downloader.py**: This script will download images from the google images and returns the list of ImageIDs it downloaded.
5. **indexing.py**: This creates a `index.csv` file which contains imageIDs with their respective color-descriptor features of database images containing images of `INRIA` and `flickr8k` dataset.
6. **load_dataset_for_training.py**: This script will load the `flickr8k dataset`, `Flickr_8k.trainImages.txt` and `descriptions.txt` file.
7. **montage.py**: This script will create a montage of result images and saves it in output folder.
8. **searcher.py**: This script will search for similar images in the database based on chi-squared function and outputs 10 most similar imageIDs.
9. **test.py**: this script is used for testing purposes. Just enter an image filename in queries folder and it returns most similar images found on web and database combined. It also returns the captions for the query image.
10. **test_caption.py**: This script will give captions for the image query.
11. **tokenizer.py**: This script will create pickle file as `src/tokenizer.p` which contains english words as numbers.
12. **train.py**: This script will train our model.

## Usage
1. Download `INRIA Holiday Dataset` which is available [here](http://lear.inrialpes.fr/people/jegou/data.php)
2. Put in the `src` folder as `dataset`.
3. Download `Flickr8k dataset` from [here](https://www.kaggle.com/shadabhussain/flickr8k) and paste the images in `dataset` folder.
4. Run `indexing.py` for indexing the database images or download trained file from [here](https://drive.google.com/file/d/1x5ytjg6_LP74NfiU_8PtqLKFhrGNa8aD/view?usp=sharing)
5. Put index.csv in the src folder
6. Image you want to query should be in `src/queries`.
7. Run `test.py` for testing.

## Examples
### Input Image
![Image](https://github.com/aakash0121/Reverse-Image-Searcher/blob/master/src/queries/4.png)

### Output Montage
![Image](https://github.com/aakash0121/Reverse-Image-Searcher/blob/master/src/output/montage_4.png)

### Input Image
![Image](https://github.com/aakash0121/Reverse-Image-Searcher/blob/master/src/queries/7.png)

### Output Image
![Image](https://github.com/aakash0121/Reverse-Image-Searcher/blob/master/src/output/montage_7.png)
