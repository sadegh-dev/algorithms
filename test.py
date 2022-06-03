names = ['charlie', 'katty', 'joe', 'matew', 'josef']
ages = [20, 35, 75, 63, 27, 43]
data = [True, 'katty', 25, '33', 'charlie', False, 35]




arr = ['a','b','c','d','b','a','g','a','d','b']

def top_one3(arr):
    key_result = list()
    result = list()
    rres = list()

    for x in arr :
        if x not in key_result :
            key_result.append(x)
            result.append(arr.count(x))


    max_ = max(result)

    for k, r in zip(key_result, result):
        if r == max_ :
            rres.append(k)

    return list((rres, max_))
