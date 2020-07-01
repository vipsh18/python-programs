def ss(l):
	for i in range(len(l)):
		if all(l[i] < l[i+1] for i in range(len(l) - 1)): break
		min_idx = i
		for j in range(i + 1, len(l)):
			if l[j] < l[min_idx]:
				min_idx = j
		l[i], l[min_idx] = l[min_idx], l[i]
	return l


l = list()
i = int(input("Enter list of elements: "))
while i != -1:
	l.append(i)
	i = int(input())
print("Sorted list:", ss(l))