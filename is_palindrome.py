#For single letter words
def is_palindrome(str):
	if str == str[::-1]:
		print('True')
	else:
		print('False')

is_palindrome('malayalam')

#For longer expressions
import re
def this_is_palindrome(str):
	front= ''.join(re.findall(r'[a-z]+', str.lower()))
	back=front[::-1]
	return front==back

this_is_palindrome('race cars')
