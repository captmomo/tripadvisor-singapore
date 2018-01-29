import re

import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize


class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self):
        """Initialize Analyzer."""
        self.positives = []
        self.negatives = []
        #https://stackoverflow.com/questions/15778747/clarifications-on-the-re-findall-method-in-python
        with open("positive-words.txt", 'r') as lines:
            for line in lines:
                positive_words = re.findall(r"[\w]+|[.,!?;]", line.rstrip())
                #print(pos_words)
                self.positives.append(positive_words)
        print(self.positives)

        with open("negative-words.txt", 'r') as lines:
            for line in lines:
                negative_words = re.findall(r"[\w]+|[.,!?;]", line.rstrip())
                #print(pos_words)
                self.negatives.append(negative_words)
        print(self.negatives)

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text.lower())

        score = 0
        #https://stackoverflow.com/questions/8275417/check-substring-match-of-a-word-in-a-list-of-words
        for token in tokens:
            for item in self.positives:
                if token in item:
                    score = score + 1
            for item in self.negatives:
                if token in item:
                    score = score - 1
        #print(score)
        return score

    def vader_analyze(self, text):
        vader = SentimentIntensityAnalyzer()
        score = vader.polarity_scores(text)
        return score['compound']

    def frequency(self, text):
        fdist1 = FreqDist(text)
        print(fdist1)
        top_50 = fdist1.most_common(50)
        return top_50

    def animal_frequency(self, input_list, raw_text):
        animals = input_list
        animals = [word.lower() for word in animals]
        #http://www.nltk.org/howto/stem.html
        stemmer = nltk.PorterStemmer()
        raw_text = raw_text
        singles = [stemmer.stem(word) for word in raw_text]
        animal_text = []
        for word in singles:
            if word in animals:
                animal_text.append(word)
            else:
                continue
        fdist1 = FreqDist(animal_text)
        top_50 = fdist1.most_common(50)
        return top_50

