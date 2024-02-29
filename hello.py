print('whats your name?')
name = input()
if name:
    print('hello ' + name)
    print('the length of your name is: ' + str(len(name)))
    print('how old are you?')
    age = input()
    print('you will be ' + str(int(age) + 1) + ' in a year.')
else:
    print('you did not enter a name')