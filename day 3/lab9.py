print('Enter username and password')
count=0
for count in range(3):
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='def' and username=='abc':
        print('logged in successfully')
        break
    else:
        print('invalid credentials')
        count += 1