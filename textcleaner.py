from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#https://machinelearningmastery.com/clean-text-machine-learning-python/
stop_words = stopwords.words('english')
filename = 'zooreviews_2.txt'
raw_file = open(filename, 'rt', encoding='utf-8')
raw_text = raw_file.read()
raw_file.close()
# split into words
tokens = word_tokenize(raw_text)
# normalize to lower case
tokens = [word.lower() for word in tokens]
# remove all tokens that are not alphabetic
words = [word for word in tokens if word.isalpha()]
# remove stopwords
words = [word for word in words if not word in stop_words]
#for word in words:
#print(word)

with open('cleantext.txt', 'w+',encoding='utf-8') as f:
    for word in words:
        f.write(word + "\n")
