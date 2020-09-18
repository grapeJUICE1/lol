
def greet():
    print('Hello')
    print('Good')
#position
def add(x , y):
    return x + y

result = add(1 , 8)
print(result)
greet()

# keyword  , default arg
def name__age(name , age=18):
    print(name)
    print(age)

name__age(name='navin' , age='78')

#variable__length arg
def sum(a ,*d):
    for i in d:
        a += i
    print(a)

sum(3 , 5 , 6)


# kwargs

def person(name , **data):
    print(name)
    print(data , data.items())

    for i,j in data.items():
        print(i , j)


person('maximilan scwarzmiller' , age='24' , phone=2322324354 , city='London')




#---------global keywords-----------#

a = 7

# def globals():
#     global a
#     a = 9
#     print('fun' , a)
#
# globals()
# print(a)
#
b = 4

def globals2():
    x = globals()['b']
    print(x)

    globals()['b'] = 8



globals2()
print(b)
