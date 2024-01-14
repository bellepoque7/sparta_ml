people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

# def check_adult(person):
#     return '성인' if person['age'] > 20 else '청소년'


# people을 하나하나 돌면서 check_adult에 넣어라
# result = map(check_adult, people)

# people 돌면서 x에 넣을 건데, x: 뒤의 값으로 return 해라.
result = map(lambda x: '성인' if x['age'] > 20 else '청소년', people)

# 아직 map이니까 list로 바꿔준다.
print(list(result))