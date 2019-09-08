class Person(object):
    #限定Person对象只能绑定_name, _age 和_gender属性

    __slots__ = ('_name', '_age', '_gender')  #__slots__的限定只对当前类的对象生效，对子类并不起任何作用


    def __init__(self, name, age):
        self._name = name
        self._age = age

    #访问器 - getter方法

    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return  self._age

    #访问器 - setter 方法
    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋。' %self._name)
        else:
            print('%s正在玩斗地主。' %self._name)


def main():
        person = Person('王大锤',12)
        person.play()
        person.age = 22
        person.play()
        person.name = 'lilu'
        person.play()
        person._gender = 'men'


if __name__ == '__main__':
    main()