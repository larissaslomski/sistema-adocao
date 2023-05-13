from random import randint
result = []
r = randint(100, 999)
if r not in result:
    result.append(r)

print(result)