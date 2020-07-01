import math
def pld(x):
	x = x.lower()
	x = x.replace(" ", "")
	for i in range(math.ceil((len(x)-1) / 2)):
		if x[i] != x[len(x) - 1 - i]:
			return "It is not a palindrome"
	return "It is a freaking palindrome"

x = input("Enter a string: ")
print(pld(x))