import re
from collections import Counter

def count_words(path):
	with open(path, encoding = 'utf-8') as file:
		all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
		all_words = [word.upper() for word in all_words]
		print('\nTotal words: ', len(all_words))
		
		word_count = Counter()
		for word in all_words:
			word_count[word]+=1
		
		print('\nTop 20 words: ')
		for word in word_count.most_common(10):
			print(word[0], '\t', word[1])
