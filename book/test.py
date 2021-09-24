def singleNumber(nums):
    new= []
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                new.append(nums[i])

    return list(set(nums)-set(new))[0]

n= singleNumber(nums=[1,1,3])
print(n)
