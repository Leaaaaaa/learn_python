class Test:
    def __init__(self , foo):
        self._foo = foo

    def _bar(self):
        print(self._foo)
        print('_bar')

def main():
    test = Test('hello')
    test._bar()
    print(test._foo)
    test._Test_bar()
    print(test._Test_foo)


if __name__ == "__main__":
    main()