from module1 import foo

foo()

from module2 import foo

foo()

import module1 as m1
import module2 as m2

m1.foo()
m2.foo()

import module3 as m3

x = int(input('x = '))
y = int(input('y = '))

print(m3.gcd(x,y))
print(m3.lcm(x,y))



