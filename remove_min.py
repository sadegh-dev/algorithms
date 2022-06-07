"""
    [9,6,2,1,3,5,7] -> 1

    remove from array and return minimum data.

"""


# Solution 1

def remove_min2(arr):
    result = arr[0]
    for x in arr[1:] :
        if x < result :
            result = x
    arr.remove(result)
    return result


# Solution 2

def remove_min(arr):
    result = min(arr)
    arr.remove(result)
    return result


##############################3

arr = [9,6,2,1,3,5,7]

print( remove_min2(arr) )
print('##############')
print(arr)