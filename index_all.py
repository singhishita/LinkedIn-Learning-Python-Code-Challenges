#find all indices of list item
#recursive call used
def index_all(listsearch, item):
	indices = list()
	for i in range(len(listsearch)):
		if listsearch[i] == item:
			indices.append([i])
		elif isinstance(listsearch[i], list):
			for index in index_all(listsearch[i], item):
				indices.append([i]+index)
	return indices
	
	
#testcase on console
test = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
index_all(test,3)
