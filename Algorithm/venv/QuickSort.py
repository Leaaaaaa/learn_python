def quicksort(arr):
    if len(arr) < 2:  #基线条件，数组只包含一个元素或数组为空
        return arr
    else:
        pivot = arr[0] #递归条件
        less = [i for i in arr[1:] if i <= pivot] #由所有小于等于基准值的元素组成的子数组
        greater = [i for i in arr[1:] if i > pivot] #由所有大于基准值的元素组成的子数组

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([4,8,19,44,2,5,1,39]))

