f = open('test.txt', 'r')
apple = f.readline()
while apple!= '':
    duck = f.readline()
    gold = f.readline()
    apple = apple.rstrip('\n')
    duck = duck.rstrip('\n')
    gold = gold.rstrip('\n')
    print(apple)
    print(duck)
    print(gold)
    print()
    apple = f.readline()