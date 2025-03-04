# basics commands
def printBasicCmds():
# hello world
    print('Hello World')

# dynamically typed identifiers
    name = 'john'
    age = 23
    salary = 22.5
    isStudent = True
    print('name:', name.upper(), 'age:', age, 'salary:', salary)

# simultaneous assignment
    product, quantity = 'book', 12
# simultaneous assignment is great for swapping variables
    trader1 = 'beans'
    trader2 = 'tea'
    print('before trade', trader1, trader2)
    trader1, trader2 = trader2, trader1
    print('after trade:', trader1, trader2)

# user input
    username = input('what is your name: ')
    print('username:', username)

# control flow
    age = int(input('what is your age: '))
    if age >= 18:
        print('adult')
    else:
        print('minor')
# loops
# for loop
    for i in range(10):
        print('for - count', i)
# while loop
    count = 3
    while count < 7:
        print('while - count', count)
        count += 1

#functions
def getName(name):
    return name

print(getName('Spencer'))

# lists, tuples, dictionaries
def getShoppingList(item1, item2, item3):
    # lists are mutable ordered
    shoppingCart = [item1,item2,item3]
    shoppingCart.append('beans')
    return shoppingCart
def getColorCombinations():
    # tuples are immutable ordered
    variations = ('red','blue','yellow')
    return variations
def getStudentId():
    students = {'alice': 1234, 'joe': 5678}
    return students

printBasicCmds()