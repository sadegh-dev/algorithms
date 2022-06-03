
# solution2 
# (MIN and MAX must be members of the list)
def limit(arr, min_=None, max_=None):
    try:
        mi = arr.index(min_)
    except:
        mi = 0
    try:
        mx = arr.index(max_)+1
    except:
        mx = len(arr)
    return arr[mi:mx]




arr = [10,20,30,40,50,60,70,80,90,100,110]
min_ = 30
max_ = 90

result = limit(arr, min_, max_)
print(result)

result = limit(arr, min_ )
print(result)

result = limit(arr, max_ = max_)
print(result)