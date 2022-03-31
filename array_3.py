# def solution(citations):
#     citations.sort()
#     n = len(citations)
#     for i in range(n):
#         if citations[i] >= n-i:
#             return n-i
#     return 0


citations = [3,0,6,1,5]

citations.sort(reverse=True)
for i in enumerate(citations,start=1):
    print(i)

answer = list(map(min, enumerate(citations, start=1)))
answer1 = max(map(min, enumerate(citations, start=1)))

print(answer, answer1)