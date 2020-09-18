import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i = 0

def inf():
    global i
    i += 1
    print('hello' , i)
    inf()

# inf()

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
