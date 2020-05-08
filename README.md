# Reverse-Image-Searcher
Reverse Image Search Engine lets you search by an image as a query and returns you similar images plus original image with their respective tags.
It searches for best results on web as well as on its database and provides 10(or as per the user) images which it predicts most similar. It uses Image Captioning(for tagging) and different descriptors for identifying each image features.
When a user uploads an image it first tries to find tags and if it passes a certain confidence threshold if starts to search for similar images on the web while another search is going on within its database. Then, all the images which it finds suitable collects in one place and again passes to the descriptor for sequencing best 10 results and put it as a montage where an user can see the results.
And it is all wrapped up under the Flask environment to get a smooth experience of searching.

## Explanation


## Usage
1. Download `INRIA Holiday Dataset` which is available [here](http://lear.inrialpes.fr/people/jegou/data.php)
2. Put in the `src` folder as `dataset`.
3. Download `Flickr8k dataset` from [here](https://www.kaggle.com/shadabhussain/flickr8k) and paste the images in `dataset` folder.
4. Run `indexing.py` for indexing the database images or download trained file from [here](https://drive.google.com/file/d/1x5ytjg6_LP74NfiU_8PtqLKFhrGNa8aD/view?usp=sharing)
5. Put index.csv in the src folder.
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
