"""
 move zeros : move zeros to end list

    [True, 0 , 'a', 20, 50, 0, 'hello', 0 , 'list']
 => [True, 'a', 20, 50,'hello','list', 0, 0, 0]

"""

def move_zeros(arr):
    num_zeros = 0
    for x in range(len(arr)):
        if arr[x] == 0 :
            num_zeros += 1
    for y in range(num_zeros) :
        arr.remove(0)
        arr.append(0)
    return arr

################################

arr1 = [True, 0 , 'a', 20, 50, 0, 'hello', 0, 'list']

result = move_zeros(arr1)

print(result)

