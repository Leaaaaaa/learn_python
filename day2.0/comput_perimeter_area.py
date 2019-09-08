import math
radius = float(input('请输入圆的半径:'))
perimeter = 2 * math.pi * radius
area1 = math.pi * (radius ** 2)
area2 = math.pi *radius *radius

print('周长 = %.2f' % perimeter)
print('面积 = %.2f' % area1)
print('面积 = %.2f' % area2)