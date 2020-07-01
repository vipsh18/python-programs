def partition(l, low, high):
	i = (low - 1)  # index of smaller element
	pivot = l[high]  # pivot
	for j in range(low, high):
		# If current element is smaller than or
		# equal to pivot
		if l[j] <= pivot:
			# increment index of smaller element
			i = i + 1
			l[i], l[j] = l[j], l[i]

	l[i + 1], l[high] = l[high], l[i + 1]
	return i + 1

def qsort(l, low, high):
	if low < high:
		pi = partition(l, low, high)
		qsort(l, low, pi-1)
		qsort(l, pi+1, high)

l = list()
i = int(input("Enter list of elements: "))
while i != -1:
	l.append(i)
	i = int(input())
qsort(l, 0, len(l) - 1)
print("Sorted list:", l)