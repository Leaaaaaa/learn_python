class Person(object):
    '''人'''

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
         self._age = age

    def play(self):
         print('%s正在玩耍。' % self._name)

    def watch(self):
        if self._age >= 18:
            print('%s正在看刺激电影' % self._name)
        else:
            print('%s正在看动画片' % self._name)


class Student(Person):

    def __init__(self, name, age, grade):
            super().__init__(name, age)
            self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
            self._grade = grade

    def study(self,course):
        print('%s的%s正在学习%s' %(self._grade, self._name, course))

class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s' %(self._name,self._title, course))

def main():
    stu = Student('lily', 20, '大一')
    stu.study('数学')
    stu.watch()
    t = Teacher('Nancy', 45, '教授')
    t.teach('python')
    t.watch()

if __name__ == '__main__':
     main()