# def solution(array, commands):
#     answer = []
#     for command in commands:
#         i,j,k = command[0], command[1], command[2]
#         new_array = array[i-1:j]
#         new_array.sort()
#         answer.append(new_array[k-1])
#     return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands= [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	

a = list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
b = map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands)

print(b)
print(a)

n = list(map(int, input()))

print(n)