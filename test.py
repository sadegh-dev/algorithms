
def search_insert(arr, item):
    try:
        return arr.index(item)
    except:
        for x in arr :
            if item <= x :
                return arr.index(x)
 

arr = [10,20,30,40,50,60,70,80,90,100,110]

item = 20
result = search_insert(arr, item)
print(result)

item = 50
result = search_insert(arr, item)
print(result)

item = 43
result = search_insert(arr, item)
print(result)
