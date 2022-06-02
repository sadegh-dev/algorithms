

def linear_search(arr, item):
    for i in arr :
        if i == item :
            return arr.index(item)
    return -1
    



ar = [20,30,60,25,98,46]
item = 90

result = linear_search(ar, item)

print(result)
