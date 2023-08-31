def abcd(nums):
    m,c = 1, 1
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] - nums[i-1] == 1:
            c += 1
        else:
            m = max(m,c)
            c = 1
    m = max(m,c)
    return m

print(abcd([0,3,7,2,5,8,4,6,0,1]))
