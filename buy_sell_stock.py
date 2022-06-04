"""
    buy - sell stock

month :
--- -1 -2 -3 -4 -5 -6 -7 -----
prices :
    [2, 6, 20, 4, 3, 2, 8] -> 2
    [7, 1, 3, 3, 10, 4] -> 4
    [9, 7, 6, 4, 3, 1] -> 0

"""

def buy_sell_stock(arr):
    statics_ = list()
    pre_ = arr[0]
    for x in arr[1:] :
        diff_ = x - pre_
        statics_.append(diff_)
        pre_ = x
    best_diff = max(statics_)
    if best_diff < 0 :
        return (0)
    else :
        return (statics_.index(best_diff)+1)


arr = [2, 6, 20, 4, 3, 2, 8]
print( buy_sell_stock(arr) )

arr = [7, 1, 3, 3, 10, 4]
print( buy_sell_stock(arr) )

arr = [9, 7, 6, 4, 3, 1]
print( buy_sell_stock(arr) )
