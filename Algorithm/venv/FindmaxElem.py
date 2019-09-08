def maxElem(list):
    if len(list) == 1:
        return list[0]
    return list[0] if list[0] > maxElem(list[1:]) else maxElem(list[1:])

print(maxElem([1,3,2,5,9,6]))