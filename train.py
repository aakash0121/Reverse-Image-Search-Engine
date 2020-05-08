import numpy as np 
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import os
from pickle import dump, load
from description_generator import load_doc
from feature_extraction import features
from tokenizer import tokenizer, max_length, vocab_size
from Model import define_model
from load_dataset_for_train import train_descriptions, train_features, train_imgs

#create input-output sequence pairs from the image description.
#data generator, used by model.fit_generator()
def data_generator(descriptions, features, tokenizer, max_length):
    while 1:
        for key, description_list in descriptions.items():
            #retrieve photo features
            feature = features[key][0]
            input_image, input_sequence, output_word = create_sequences(tokenizer, max_length, description_list, feature)
            yield [[input_image, input_sequence], output_word]

def create_sequences(tokenizer, max_length, desc_list, feature):
    X1, X2, y = list(), list(), list()
    # walk through each description for the image
    for desc in desc_list:
        # encode the sequence
        seq = tokenizer.texts_to_sequences([desc])[0]
        # split one sequence into multiple X,y pairs
        for i in range(1, len(seq)):
            # split into input and output pair
            in_seq, out_seq = seq[:i], seq[i]
            # pad input sequence
            in_seq = pad_sequences([in_seq], maxlen=max_length)[0]
            # encode output sequence
            out_seq = to_categorical([out_seq], num_classes=vocab_size)[0]
            # store
            X1.append(feature)
            X2.append(in_seq)
            y.append(out_seq)
    return np.array(X1), np.array(X2), np.array(y)

if __name__ == "__main__":

    # train our model
    print('Dataset: ', len(train_imgs))
    print('Descriptions: train=', len(train_descriptions))
    print('Photos: train=', len(train_features))
    print('Vocabulary Size:', vocab_size)
    print('Description Length: ', max_length)

    model = define_model(vocab_size, max_length)
    epochs = 10
    steps = len(train_descriptions)

    # making a directory models to save our models
    os.mkdir("src/models")
    for i in range(epochs):
        generator = data_generator(train_descriptions, train_features, tokenizer, max_length)
        model.fit_generator(generator, epochs=1, steps_per_epoch= steps, verbose=1)
        model.save("src/models/model_" + str(i) + ".h5")