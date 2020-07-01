# Number of ways for getting to the top from the bottom

def num_ways(n):
    if n == 0 or n == 1: return 1
    nums = []
    nums.append(1)
    nums.append(1)
    for i in range(2, n+1):
        nums.append(nums[i-1] + nums[i-2])
    return nums[n]

def num_ways_X(n):
    if n == 0: return 1
    nums = []
    nums.append(1)
    for i in range(1, n+1):
        total = 0
        for j in {1, 3, 5}:
            if i - j >= 0:
                total += nums[i - j]
        nums.append(total)
    return nums[n]

print(num_ways_X(7))