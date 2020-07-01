def linear_search(arr, key):
    for i in range(len(arr)):
        if key == arr[i]:
            return f"{key} found at index {i}"
    return "Key not found"


arr = list()
i = int(input("Enter list of elements: "))
while i != -1:
	arr.append(i)
	i = int(input())
key = int(input("Enter key to search: "))
print(linear_search(arr, key))