name = input('Enter name:')
print('menu')

choice = input('Enter choice Q or H or G:')

while choice != 'Q':
    if choice == 'H':
        print('hello,name', name)
    elif choice == 'G':
        print('goodbye,name', name)
    else:
        print('invalid message')
        print('menu')

    choice = input('Enter choice Q or H or G:')

print('finished')
