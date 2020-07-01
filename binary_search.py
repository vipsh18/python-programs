def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if key == arr[mid]:
            return f"{key} found at index {mid}"
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return "Key not found"


arr = list()
i = int(input("Enter list of elements: "))
while i != -1:
	arr.append(i)
	i = int(input())
key = int(input("Enter key to search: "))
arr.sort()
print(binary_search(arr, key))