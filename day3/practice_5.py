from random import randint

answer = randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入数字：'))
    if number < answer :
        print('大一点')
    elif number >answer :
        print('小一点')
    else:
        print('congratulations!')
        break

print('你总共猜对了%d次' %counter)
if counter > 7:
    print('你太笨啦')
