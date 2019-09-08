import sys
def foo():  #列表操作
  list1 = [1, 3, 5,7, 100]
  print(list1)
  list2 = ['helllo'] * 5
  print(list2)
  #计算列表长度（元素个数）
  print(len(list1))
  #下标（索引）运算
  print(list1[-1])
  print(list1[-3])
  list1[2] = 300
  print(list1)
  list1.append(200)
  print(list1)
  list1.insert(2,400)
  print(list1)
  list1 += [1000,2000]
  print(list1)
  list1.clear()
  print(list1)

def fol():  #列表切片
    fruits = ['grape' , 'apple' , 'strawbarry' , 'waxberry']
    fruits += ['pitaya' , 'pear' , 'mango']
    #循环遍历列表元素
    for fruit in fruits:
        print(fruit.title(), end = ' ')
    print()
    #列表切片
    fruits2 = fruits[1:4]
    print(fruits2)
    fruits3 = fruits[:]
    print(fruits3)
    fruits4 = fruits[-3:-1]
    print(fruits4)
    fruits5 = fruits[::-1]
    print(fruits5)
    print()

def fll():#对代码排序
    list1 = ['orange' , 'apple' , 'zoo' , 'internationallization' , 'blueberry']
    list2 = sorted(list1)
    #sorted函数返回列表排序后的拷贝不会修改传入的列表
    #函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1,reverse=True)
    #通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表序列
    list4 = sorted(list1, key = len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    #给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)
    print()


def fii():#生成语法创建列表
    f = [x for x in range(1 , 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)
    #用列表的生成表达式语法创建列表容器
    #用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(1 , 100)]
    print(sys.getsizeof(f))  #查看对象占用内存空间
    print(f)
    #请注意下面的代码创建的不是一个列表而是一个生成对象器
    #通过生成器可以获取到数据但他不占用额外的空间存储数据
    #每次需要数据的时候就通过内部的运算得到数据（需要花额外的时间）
    f = (x ** 2 for x in range(1 , 100))
    print(sys.getsizeof(f))  #相比生成式生成器不占用存储数据的空间
    print(f)
    for val in f:
        print(val)

def fib(n):
    a , b = 0 , 1
    for _ in range(n):
        a ,b = b ,a + b
        yield a

def fbb():
    for val in fib(20):
        print(val)


foo()
fol()
fll()
fii()
fbb()