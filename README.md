# Reverse-Image-Searcher
This project takes a query as an Image then find similar images and results in a montage of 10 similar images to the original query image.

## Usage
1. It is trained on `INRIA Holiday Dataset` which is available [here](http://lear.inrialpes.fr/people/jegou/data.php)
2. Download above dataset and put in the `src` folder.
3. Run `indexing.py` for indexing the database images or download trained file from [here](https://drive.google.com/file/d/1JhIJ16hkOIhGZ85MIOUnpZnqlYNWqp8f/view?usp=sharing)
4. Put index.csv in the src folder.
5. Image you want to query should be in `src/queries`.
6. Run `test.py` for testing.

## Examples
### Input Image
![Image](https://github.com/aakash0121/Reverse-Image-Searcher/blob/master/src/queries/4.png)

### Output Montage
![Image](https://github.com/aakash0121/Reverse-Image-Searcher/blob/master/src/output/montage_4.png)

### Input Image
![Image](https://github.com/aakash0121/Reverse-Image-Searcher/blob/master/src/queries/7.png)

### Output Image
![Image](https://github.com/aakash0121/Reverse-Image-Searcher/blob/master/src/output/montage_7.png)
