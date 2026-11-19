def TargetSum(nums,target):
    left = 0
    right = len(nums)-1
    result = []
    while left<right:
        total = nums[left]+nums[right]
        if total==target:
            result.append([nums[left],nums[right]])
            left+=1
            right-=1
        elif total<target:
            left+=1
        else:
            right-=1
    return result
    
nums = list(map(int,input().split()))
target = int(input("Enter Target"))
print(TargetSum(nums,target))