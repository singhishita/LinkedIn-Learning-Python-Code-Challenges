def sort_words(input):
	inp = input.split()
	words = [x.lower() for x in inp]
	words.sort()
	for i in words:
		print(i)

sort_words('PINEAPPLE Grapes oraNge APPLE meloN')
