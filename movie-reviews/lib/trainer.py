from nlp.lib.data import ReviewHandler
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import re
#import nltk.data

#nltk.download()
# Load the punkt tokenizer
#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 

# Convert document to a sequence of words
# Optionally remove stop words, false by default
# Return list
def review_to_wordlist(review, remove_stopwords=False):
    review_text = BeautifulSoup(review).get_text()
    review_text = re.sub('[^a-zA-Z]', '', review_text)
    words = review_text.lower().split()

    if remove_stopwords:
    	stops = set(stopwords.words('english'))
    	words = [w for w in words if not w in stops]

    return words

# Split review into parsed sentences
# Returns list
def review_to_sentences(review, tokenizer, remove_stopwords=False):
	# spilt paragraphs into sentences
	raw_sentences = tokenizer.tokenize(review.strip())

	sentences = []
	for raw_sentence in raw_sentences:
		if len(raw_sentence) > 0:
			sentences.append(review_to_wordlist(raw_sentence, remove_stopwords ))

	return sentences

sentences = []

