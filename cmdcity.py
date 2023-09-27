import math

h = 10 #int(input())
w = 15 #int(input())
simvol = '#'
space = '_'

a = w // 2
math.ceil(a)
for i in range(a):
    print(space * (a-1-i) + simvol * (1-i) + simvol * (a+2+i))

for i in range(h - 2):
    print(simvol, ' ' * (w - 2), simvol, sep='')
print(simvol * w)