year = int(input('请输入年份：'))

flag1 = year%400 ==0
flag2 = year%4==0 and year%100 !=0

if flag1 or flag2:
    print('%d是闰年' % year)
else:
    print("%d不是闰年" %year)