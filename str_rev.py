def str_rev(x):
	y = ""
	for i in range((len(x))):
		y = y + x[len(x) - 1 - i]
	return y

x = input("Enter a string: ")
print("String Reversed: ", str_rev(x))