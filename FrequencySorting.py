def hashmap(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num,0)+1
    return frequency
nums = list(map(int,input().split()))
freq = hashmap(nums)
result = sorted(nums,key=lambda x:(freq[x],x))
print(result)