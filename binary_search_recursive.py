def binary_search_recursive(arr, key, low, high):
    if low > high:
        return "Key not found"
    else:
        mid = (low + high) // 2
        if key == arr[mid]:
            return f"{key} found at index {mid}"
        elif key < arr[mid]:
            return binary_search_recursive(arr, key, low, mid-1)
        else:
            return binary_search_recursive(arr, key, mid+1, high)


arr = list()
i = int(input("Enter list of elements: "))
while i != -1:
	arr.append(i)
	i = int(input())
key = int(input("Enter key to search: "))
arr.sort()
high = len(arr) - 1
print(binary_search_recursive(arr, key, 0, high))