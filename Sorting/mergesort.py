def mergesort(lst, low, high):
	if low < high:
		m = low + (high - low)//2
		mergesort(lst, low, m)
		mergesort(lst, m+1, high)
		merge(lst, low, m, high)

def merge(lst, l, m, h):
	# store temp array
	lst1 = lst[l:m+1]
	lst2 = lst[m+1:h+1]

	i = l
	# find the smallest, pop it out then set back into lst
	while lst1 and lst2:
		if lst1[0] > lst2[0]:
			lst[i] = lst2[0]
			i+=1
			lst2.pop(0)
		else:
			lst[i] = lst1[0]
			i+=1
			lst1.pop(0)

	# one of the temp array is empty
	if not lst1:
		while lst2:
			lst[i] = lst2[0]
			i+=1
			lst2.pop(0)

	if not lst2:
		while lst1:
			lst[i] = lst1[0]
			i+=1
			lst1.pop(0)



if __name__ == '__main__':
	test = [3, 7, 2, 4, 5, 1, 9, 8]
	mergesort(test, 0, len(test)-1)
	print(test)