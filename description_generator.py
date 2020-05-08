import string

# load text file into memory
def load_doc(filename):
    # opening file
    file = open(filename, 'r')
    text = file.read()
    file.close()
    # text variable contains all the information in string format
    return text

# get all images with their captions
def all_img_captions(filename):
    file = load_doc(filename)
    captions = file.split('\n')

    # this dictionary contains image ID as key and values as list of captions
    descriptions ={}

    for caption in captions[:-1]:
        img, caption = caption.split('\t')

        if img[:-2] not in descriptions:
            descriptions[img[:-2]] = list(caption)
        else:
            descriptions[img[:-2]].append(caption)

    return descriptions

# this is for cleaning the data i.e all lower case letters, removing digits, remove punctuations
def cleaning_text(descriptions):
    table = str.maketrans('','',string.punctuation)

    for img,caps in descriptions.items():
        for i,img_caption in enumerate(caps):

            img_caption.replace("-"," ")
            desc = img_caption.split()

            # converts to lowercase
            desc = [word.lower() for word in desc]

            # remove punctuation from each token
            desc = [word.translate(table) for word in desc]

            # remove hanging 's and a 
            desc = [word for word in desc if(len(word)>1)]

            # remove tokens with numbers in them
            desc = [word for word in desc if(word.isalpha())]

            # convert back to string
            img_caption = ' '.join(desc)

            descriptions[img][i]= img_caption

    return descriptions

# this is used to seperate all unique words and create a vocabulary from descriptions
def text_vocabulary(descriptions):
    # build vocabulary of all unique words
    vocab = set()
    for key in descriptions.keys():
        [vocab.update(d.split()) for d in descriptions[key]]
    return vocab

#All descriptions in one file as descriptions.txt
def save_descriptions(descriptions, filename):
    lines = list()
    for key, desc_list in descriptions.items():
        for desc in desc_list:
            lines.append(key + '\t' + desc )
    data = "\n".join(lines)
    file = open(filename,"w")
    file.write(data)
    file.close()

# Set these path according to project folder in you system
dataset_text = "src/flickr8k/Flickr_TextData"

#we prepare our text data
filename = dataset_text + "/" + "Flickr8k.token.txt"

#loading the file that contains all data
#mapping them into descriptions dictionary img to 5 captions
descriptions = all_img_captions(filename)
print("Length of descriptions =" ,len(descriptions))

#cleaning the descriptions
clean_descriptions = cleaning_text(descriptions)

#building vocabulary 
vocabulary = text_vocabulary(clean_descriptions)
print("Length of vocabulary = ", len(vocabulary))

#saving each description to file 
save_descriptions(clean_descriptions, "src/descriptions.txt")
