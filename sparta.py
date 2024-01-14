participant = ["mike", "lisa", "tom", "lisa"]
completion = ["tom", "mike", "lisa"]
x = []

# 1번 참가자, 2번 완주자
# 1번이지만 2번을 못한 사람, 차집합 -> 동명이인 때문에 ㄴ
# 함수명은 find_non_completer

def find_non_completer(a, b):
    set(x) == set(a) - set(b)
    return set(x)


result = find_non_completer(participant, completion)

print(result)