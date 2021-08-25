'''
- 서로 다른 정수가 담긴 두 개의 리스트를 비교하여 li안에 있는 정수가 li2에도 담겨있다면 그 정수를 배제하세요.
서로 겹치지 않는 정수만 담긴 새로운 리스트를 생성해 보세요.
'''
li = [1, 2, 3, 4, 5, 6, 7]
li2 = [1, 3, 8, 4, 5, 7, 101]

# 집합 연산자를 쓴 방법
li_set = set(li)
li2_set = set(li2)

new_set = li_set ^ li2_set
new_list = list(new_set)
new_list.sort()
print(new_list)

# 다른 방법
li.sort()
li2.sort()

both = set()

for i in range(len(li)):
    for j in range(len(li2)):
        if li[i] == li2[j]:
            both.add(li[i])

for i in both:
    li.remove(i)
    li2.remove(i)

li3 = li + li2
li3.sort()
print(li3)