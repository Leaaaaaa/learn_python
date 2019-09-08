#使用集合
def main():
    set1 = {1, 2 , 3 , 3, 2,}
    print(set1)
    print('Length = ', len(set1))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set2.add(5)
    set2.update([11,12])
    print(set1)
    print(set2)
    set2.discard(5)
    #remove的元素如果不存在会引发keyerror
    if 4 in set2:
        set2.remove(4)
    print(set2)
    #将元组转换成集合
    set3 = set((1, 2, 3, 3, 3, 1))
    print(set3.pop())
    print(set3)
    #集合的交集、并集、差集、对称差运算
    print(set1 & set2)
    #print(set1.intersection(set2))交集
    print(set1 | set2)
    #print(set1.union(set2)) 并集
    print(set1 - set2)
    #print(set1.defference(set2))差集
    print(set1 ^ set2)
    #print(set1.symmetric_difference(set2))对称差
    #判断子集和超集
    print(set2 <= set1)
    #print(set2.issubset(set1))
    print(set3 <= set1)
    #print(set3.issubset(set1))
    print(set1 >= set2)
    #print(set1.issuperset(set2))
    print((set1 >= set3))
    #print(set1.issuperset(set30）

if __name__ == '__main__':
    main()