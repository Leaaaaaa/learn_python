def foo():
    pass
def bar():
    pass
'''

if __name__  == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
'''
def gcd(x,y): #最大公约数
    (x,y)=(y,x) if x > y else (x,y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x,y): #最小公倍数
    return x * y // gcd(x,y)

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

