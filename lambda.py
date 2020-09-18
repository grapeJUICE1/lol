from functools import reduce

add = lambda a , b : a + b

print(add(2 ,6))

nums = [2 , 65 , 6 , 87 , 56 , 43 , 98 , 21 , 90 , 21 , 34]

evens = list(filter(lambda a: a % 2 == 0,nums))
odds = list(filter(lambda a: a % 2 != 0,nums))
doubles = list(map(lambda a: a * 2 ,nums))
sum = reduce(lambda a,b: a +  b , nums)

print(evens , odds)
print(doubles)
print(sum)
