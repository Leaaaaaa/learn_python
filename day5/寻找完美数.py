for num in range(1000000):
    m = num
    count = 0
    for i in range(1,m-1):
            if num % i ==0:
                count += i
    if count == num:
       print('%d是完美数' % num)