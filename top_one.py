def top_one(arr):
    nums = []
    repeat = []
    for x in arr:
        if x not in nums :
            nums.append(x)
            repeat.append(1)
        else :
            y = nums.index(x)
            num = repeat[y] + 1
            repeat[y] = num
    
    maxo = max(repeat)
    result = []
    i = 0
    for x in repeat :
        if x == maxo :
            result.append(nums[i])
        i += 1
    return list((result,maxo))
    #return list((nums,repeat))


print( top_one([7,2,7,2,1]) )
print( top_one([1,2,7,2,1,4,7]) )
