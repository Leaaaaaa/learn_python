from random import randint
def roll_dice(n=2):
    '''
    摇色子
    :param n: 色子的个数
    :return: n颗色子的点数之和
    '''
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

def add(a=0, b=0, c=0):
    return a+b+c

def add_2(*args):
    total = 0
    for val in args:
        total += val
    return total

print(roll_dice())
print(roll_dice(1))
print(roll_dice(3))
print(add(1))
print(add(1,2))
print(add(1,2,3))
print(add(c=20,b=40,a=10))
print(add_2())
print(add_2(1))
print(add_2(1,2))
print(add_2(4,0,24,55))