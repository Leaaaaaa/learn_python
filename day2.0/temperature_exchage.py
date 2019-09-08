#将华氏度转化为摄氏度

F = float (input( '请输入华氏度：'))
C = (F - 32) / 1.8

print('%.1f华氏度 = %.1f 摄氏度' %(F,C))


print('请输入摄氏度')
c = float(input())
print(c*1.8+32)
