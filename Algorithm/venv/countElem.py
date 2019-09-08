def coutElem(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1+coutElem(arr[1:])

print(coutElem([1,2,2,2,4,5]))