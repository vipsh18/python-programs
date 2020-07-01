def isort(l):
	for i in range(1, len(l)):
		key = l[i]
		j = i - 1
		while j >= 0 and key < l[j]:
			l[j+1] = l[j]
			j -= 1
		l[j+1] = key
	return l


def isort_dec(l):
	for i in range(1, len(l)):
		key = l[i]
		j = i - 1
		while j >= 0 and key > l[j]:
			l[j+1] = l[j]
			j -= 1
		l[j+1] = key
	return l


l = list()
i = int(input("Enter list of elements: (to stop enter -1)"))
while i != -1:
	l.append(i)
	i = int(input())

choice = int(input("Enter Your Choice:\n1.Increasing Order\n2.Decreasing Order\n"))
if choice == 1: print("Sorted List:", isort(l))
else: print("Sorted List:", isort_dec(l))