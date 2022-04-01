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



print( search_insert([1,3,5,6], 0) )
print( search_insert([1,3,5,6], 3) )
print( search_insert([1,3,5,6], 2) )
print( search_insert([1,3,5,6], 5) )
print( search_insert([1,3,5,6], 7) )
