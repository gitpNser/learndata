n = int(input('pls input a number:'))
i = 2
while n != 1:
    while n % i == 0:
        n //= i
        if n == 1:
            print('%d' % i)
        else:
            print('%d *' % i, end = ' ')
    i +=1
