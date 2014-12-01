//Details
	takes in linked-list
	base case: for empty list

def listHelper(L) :

	int count = 0
	while(L[-1] != [])
		++count
		L[-1] = L[-1][-1]
	return count


def reverse(L) :

	if L.length = 0
		return L
	elif L[-1] = []
		return L
	else
		while()
		int first = 0
		int last = -1
		int half = listHelper(L) / 2
		if(L[last] = [])
			L[first] = L[0][last]
			++first
			--last
			if (first == half)
				return L
				
