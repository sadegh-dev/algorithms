def limit (arr, min=None, max=None):
    result = []
    if max and min :
        for x in arr :
            if x >= min and x <= max :
                result.append(x)
    elif max and (not min) :
        for x in arr :
            if x <= max :
                result.append(x)
    elif min and (not max) :
        for x in arr :
            if x >= min :
                result.append(x)
    else :
        result = arr.copy()
    return result


print(limit([1,3,4,5,6,7,8,9,10], 3, 8))
print(limit([1,3,4,5,6,7,8,9,10], 7))
print(limit([1,3,4,5,6,7,8,9,10], max=6))
