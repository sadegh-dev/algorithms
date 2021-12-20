# My Solution
def top_one(arr):
    nums = []
    repeat = []
    for x in arr:
        if x not in nums :
            nums.append(x)
            repeat.append(1)
        else :
            y = nums.index(x)
            repeat[y] += 1
    
    maxo = max(repeat)
    result = []
    i = 0
    for x in repeat :
        if x == maxo :
            result.append(nums[i])
        i += 1
    return list((result,maxo))



# Solution2 - Use Dictionary

def top_one2(arr):
    repeat = {}
    result = []
    maxo = 0

    for x in arr :
        if x in repeat :
            repeat[x] +=1
        else :
            repeat[x] = 1
        
    maxo = max(repeat.values())

    for x in repeat.keys():
        if repeat[x] == maxo :
            result.append(x)
    
    return list((result, maxo))



print( top_one([7,2,7,2,1]) )
print( top_one([1,2,7,2,1,4,7]) )

print( top_one2([7,2,7,2,1]) )
print( top_one2([1,2,7,2,1,4,7]) )