message = 'Hello word'

print('Hello World')

print(message)

print(len(message))

print(message[0])

print(message[0:5])

print(message[6:])

print(message.lower())

print(message.upper())

print(message.count('Hello'))

print(message.find('Hello'))

print(message.find('universe'))

new_message = message.replace('Word', 'Universe')

print(new_message)

greeting = 'Hello'
name = 'Michael'

message2 = greeting + ', ' + name + '. Welcome!'

print(message2)

message3 = '{}, {}. Welcome!'.format(greeting, name)

print(message3)

message4 = f'{greeting}, {name}. Welcome!'

print(message4)

print (dir(name))

print(help(str))


