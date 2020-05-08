from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.applications.xception import Xception
from keras.models import load_model
from pickle import load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# in_path = "test_input/"

def extract_features(filename, model):
    image = Image.open(filename)
    image = image.resize((299,299))
    image = np.array(image)
    # for images that has 4 channels, we convert them into 3 channels
    if image.shape[2] == 4: 
        image = image[..., :3]
    image = np.expand_dims(image, axis=0)
    image = image/127.5
    image = image - 1.0
    feature = model.predict(image)
    return feature

def word_for_id(integer, tokenizer):
 for word, index in tokenizer.word_index.items():
     if index == integer:
         return word
 return None


def generate_desc(model, tokenizer, photo, max_length):
    in_text = 'start'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        pred = model.predict([photo,sequence], verbose=0)
        pred = np.argmax(pred)
        word = word_for_id(pred, tokenizer)
        if word is None:
            break
        in_text += ' ' + word
        if word == 'end':
            break
    return in_text

def returns_caption(in_path):
    max_length = 32
    tokenizer = load(open("src/tokenizer.p","rb"))
    model = load_model('src/models/model_9.h5')
    xception_model = Xception(include_top=False, pooling="avg")

    # print(filename)
    photo = extract_features(in_path, xception_model)
    img = Image.open(in_path)

    description = generate_desc(model, tokenizer, photo, max_length)
    print("\n\n")
    stopwords = ['start', 'end']
    for words in stopwords:
        description = description.replace(words, "")
    # print(description)
    # img.show()
        
    return description