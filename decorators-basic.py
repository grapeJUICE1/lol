def div(a,b):
    return a / b

def smart_div(func):
    def inner(a , b):
        if a < b:
            a , b = b , a
        return func(a , b)
    return inner


div = smart_div(div)
print(smart_div(div)(2,4))
print(div(2,4))
