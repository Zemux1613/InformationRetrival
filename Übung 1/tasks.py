#import libraries
import nltk
import regex as re
from nltk import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def preprocess(text):
    regex = re.compile('[^a-zA-Z\s]')
    # replace period(.) with a space to separate the two sentences
    text_returned = text.replace('.', ' ', )
    # tokenize text
    text_returned = re.sub(regex, '', text_returned)

    # tokenize text
    text_tokens = word_tokenize(text_returned)

    # remove stopwords
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words('english')]

    # lemmatize tokens
    nltk.download('wordnet')
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()

    lem_tokens = [lemmatizer.lemmatize(word) for word in tokens_without_sw]

    return lem_tokens


vocab = []
# read text file
fileHandle = open("./US_pres_speeches/trumpspeech.txt", mode="r", encoding="utf-8")
file = fileHandle.read()
trump_speech = file
processed_tokens = preprocess(trump_speech)
# build vocabulary

for token in processed_tokens:
    if token not in vocab:
        vocab.append(token)

print('Length of vocabulary: ', len(vocab))