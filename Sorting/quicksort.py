import random

# make sure check for empty lst
def quicksort(lst, low, high):
	if low < high:
		pivot = partition(lst, low, high)
		quicksort(lst, low, pivot-1)
		quicksort(lst, pivot+1, high)

def swap(lst, i, j):
	temp = lst[i]
	lst[i] = lst[j]
	lst[j] = temp

def partition(lst, low, high):
	pivot = lst[high]
	i = low
	for j in range(low, high):
		if lst[j] < pivot:
			swap(lst, i, j)
			i+=1

	swap(lst, i, high)
	return i

if __name__ == "__main__":
	test = [3, 7, 2, 1, 5, 4, 6]
	quicksort(test, 0, len(test)-1)
	print(test)