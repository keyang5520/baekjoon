from __future__ import print_function


numbers = [0,0,0]

numbers = list(map(str, numbers))

numbers.sort(key=lambda x: x*3 , reverse=True)
answer = ''.join(numbers)
answer1 = str(int(''.join(numbers)))
print(numbers)

print(answer,answer1)