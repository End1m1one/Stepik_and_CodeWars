def say_hello(name, city, state):
    return 'Hello, ' +  ' '.join(name) + '!' + ' Welcome to ' + ''.join(city)  + ',' + ''.join(state)




print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))