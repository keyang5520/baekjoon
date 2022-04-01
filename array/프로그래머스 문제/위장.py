def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        clothes_type[t] = clothes_type.get(t, 1) + 1
        
    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1