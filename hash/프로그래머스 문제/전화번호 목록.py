phone_book = ["119", "97674223", "1195524421"]	

answer = True
d = {}
for number in phone_book:
    d[number] = 1

for number in phone_book:
    temp = ''
    for num in number:
        temp += num
        print(num)
        if temp in d and temp != number:
            answer = False

print(answer)

