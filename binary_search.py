"""
Log2(N)

"""

def binary_search(the_list, value):
    left_edge , right_edge = 0 , len(the_list) -1
    while left_edge <= right_edge:
        middle = left_edge + (right_edge) -1
        if the_list[middle] == value :
            return middle
        





a_list = [10,20,30,40,50,60,70,80,90]
value = 40
