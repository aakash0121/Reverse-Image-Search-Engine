# Reverse-Image-Searcher
This project takes a query as an Image then find similar images and results in a montage of 10 similar images to the original query image.

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
