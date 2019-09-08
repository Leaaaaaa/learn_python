from random import randint

n = []
for num in range(100,999):
    m = num
    count1 = num%10
    num //= 10
    count2 = num%10
    num //=10
    count3 = num %10
    if m == count1**3 + count2**3 + count3**3:
       print('%d是水仙花数' % m)



