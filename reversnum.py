n = int(input('pls input a number:'))
m = n
s = 0
while n != 0:
    s = s * 10 + n % 10
    n //= 10
print('the revers number is %d:%d' % (m, s)) 
