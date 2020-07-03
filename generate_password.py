import secrets
#instead of random module, the Python Documentation advices the use of secrets module for security purposes

def generate_passphrase(num_words):
	with open('diceware.wordlist.asc', 'r') as file:
		lines = file.readlines()[2:7778]
		word_list = [line.split()[1] for line in lines]
	
	words = [secrets.choice(word_list) for i in range(num_words)]
	return ' '.join(words)

#Solution by Barron Stone, the Instructor
