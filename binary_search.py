
# None recursive function
def binary_search(arr, item):
    a = []
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
        mid = len(arr) // 2
        if arr[mid] < item :
            a.extend(arr[:mid], item)
            binary_search(a, item)
        else :
            a.extend(arr[mid:], item)
            binary_search(a, item)


#################################
ar = [10]
item = 10

result = binary_search(ar, item)

print(result)