import os 
import nltk.data
import pandas as pd

#absolute file paths
file_dir = os.path.dirname(__file__) 

#training data
#filename_1 = os.path.join(file_dir, '../data/labeledTrainData.tsv')
#filename_1 = os.path.abspath(os.path.realpath(filename_1))
#train = pd.read_csv(filename_1, header=0, delimiter="\t", quoting=3)

#test data
#filename_2 = os.path.join(file_dir, '../data/testData.tsv')
#filename_2 = os.path.abspath(os.path.realpath(filename_2))
#test = pd.read_csv(filename_2, header=0, delimiter="\t", quoting=3)

#unlabeled data
#filename_3 = os.path.join(file_dir, '../data/unlabeledTrainData.tsv')
#filename_3 = os.path.abspath(os.path.realpath(filename_3))
#unlabeled_train = pd.read_csv(filename_3, header=0, delimiter="\t", quoting=3)

msg = 'Read {train} labeled train reviews, {test} labeled test reviews, and {unlabeled} unlabeled reviews'.format(
	train=train['review'].size,
	test=test['review'].size,
	unlabeled= unlabeled_train['review'].size
	) 
print(msg)
print(train['review'][0])

class ReviewHandler(object):
	def __init__(self, train_file, test_file, unlabeled_train_file):
		train_file = os.path.join(file_dir, train_file)
		train_file = os.path.abspath(os.path.realpath(train_file))

		test_file = os.path.join(file_dir, test_file)
		test_file = os.path.abspath(os.path.realpath(test_file))

		unlabeled_train_file = os.path.join(file_dir, unlabeled_train_file)
		unlabeled_train_file = os.path.abspath(os.path.realpath(unlabeled_train_file))
		
		self.train_file = train_file, 
		self.test_file = test_file,
		self.unlabeled_train_file = unlabeled_train_file

		#download
		nltk.download()

	def read(self):
		train = pd.read_csv(self.train_file, header=0, delimiter="\t", quoting=3)
		test = pd.read_csv(self.test_file, header=0, delimiter="\t", quoting=3)
		unlabeled_train = pd.read_csv(self.unlabeled_train_file, header=0, delimiter="\t", quoting=3)
		return train, test, unlabeled_train

	def tokenizer():
		tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 
		return tokenizer

