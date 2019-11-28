while True:
    try:
        q = int(input('pls input the quantity: '))
        p = int(input('pls input the price:'))
        print('pay: %d' % (q * p))
        break
    except Exception as e:
        print(e)
        print('pls input valid number')
