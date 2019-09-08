def sum(arr):
    if len(arr) == 0:
        return 0
    inx = 0
    total = arr.pop(inx) #移除列表一个元素（默认最后一个）并返回它的值
    if len(arr) == 0:
        return total
    else:
        return total + sum(arr)

print(sum([1,2,3,4,5]))

