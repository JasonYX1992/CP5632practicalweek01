

shipping = float(input('Enter shipping:'))

if shipping > 100:
    shipping = shipping * 0.9
    print('shipping', shipping)
elif 0 <= shipping <= 100:
    shipping = shipping * 1
    print('shipping', shipping)
else:
    print('Invalid number of item')







