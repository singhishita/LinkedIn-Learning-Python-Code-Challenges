#script
import pickle
def save_dict(input_dict, file_location):
	with open(file_location, 'wb') as file:
		pickle.dump(input_dict, file)

def read_dict(file_path):
	with open(file_location, 'rb') as file:
		return pickle.load(file)

#console
from dictionary import *
test_dict = {1: 'alphabet', 2: 'google', 3: 'sundar pichai', 4: 'ceo'}
save_dict(test_dict,'test_dict.pickle')

recovered = read_dict('test_dict.pickle')

print(recovered)

#Similar implementation for JSON

import json
#write to a file
myfile.write(json.dumps(mydict))
#read a file
mydict = json.loads(myfile.read())
