def bs(l):
	for i in range(len(l)):
		if all(l[i] < l[i+1] for i in range(len(l) - 1)): break
		for j in range(len(l) - 1):
			if l[j+1] < l[j]:
				l[j], l[j+1] = l[j+1], l[j]
	return l


l = list()
i = int(input("Enter list of elements: "))
while i != -1:
	l.append(i)
	i = int(input())
print("Sorted list:", bs(l))