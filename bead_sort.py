
def bead_sort(arr):
    result = list()
    result.append(arr[0])
    for x in arr[1:] :
        for a in result :
            if x <= a :
                result.insert(result.index(a), x)
                break
        else :
            result.append(x)
    return result 
        


arr = [6,80,5,20,3,10,9,20]

result = bead_sort(arr)

print(result)