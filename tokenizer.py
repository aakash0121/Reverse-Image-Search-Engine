from keras.preprocessing.text import Tokenizer
from pickle import dump, load
from description_generator import descriptions
from load_dataset_for_train import train_descriptions

#converting dictionary to clean list of descriptions
def dict_to_list(descriptions):
    all_desc = []
    for key in descriptions.keys():
        [all_desc.append(d) for d in descriptions[key]]
    return all_desc

#creating tokenizer class 
#this will vectorise text corpus
#each integer will represent token in dictionary
def create_tokenizer(descriptions):
    desc_list = dict_to_list(descriptions)
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(desc_list)
    return tokenizer

#calculate maximum length of descriptions
def max_length(descriptions):
    desc_list = dict_to_list(descriptions)
    return max(len(d.split()) for d in desc_list)

if __name__ == "__main__":
    # give each word an index, and store that into tokenizer.p pickle file
    tokenizer = create_tokenizer(train_descriptions)
    dump(tokenizer, open('src/tokenizer.p', 'wb'))
    vocab_size = len(tokenizer.word_index) + 1
    print(vocab_size) 

    max_length = max_length(descriptions)
    print(max_length)