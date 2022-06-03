# Solution 1

def search_insert(arr, num):
    le = len(arr)
    result = None

    for i in range(0,le) :
        if num < arr[i]:
            result = i
            break
        elif num == arr[i]:
            result = i 
            break
    
    if result == None :
        result = le

    return result


# Solution 2

def search_insert2(arr, item):
    try:
        return arr.index(item)
    except:
        for x in arr :
            if item <= x :
                return arr.index(x)
    return len(arr)
 


print( search_insert2([1,3,5,6], 0) )
print( search_insert2([1,3,5,6], 3) )
print( search_insert2([1,3,5,6], 2) )
print( search_insert2([1,3,5,6], 5) )
print( search_insert2([1,3,5,6], 7) )
