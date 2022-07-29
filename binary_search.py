# Recursive Function
def binary_search(arr, item):
    ll = len(arr)
    if ll == 1 :
        if arr[0] == item :
            return True
        else :
            return False
    elif ll == 2 :
        if arr[0] == item or arr[1] == item :
            return True
        else :
            return False
    else :
        mid = ll // 2
        if arr[mid] == item :
            return True
        elif item < arr[mid] :
            #print(arr[:mid])
            return binary_search(arr[:mid], item)
        else :
            #print(arr[mid:])
            return binary_search(arr[mid:], item)


#############################
ar = [10,20,30]
item = 35

result = binary_search(ar, item)

print(result)



