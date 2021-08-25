'''
리스트 내부 요소 삭제

1. remove(): 삭제할 값을 직접 지정하여 삭제
2. 내장함수 del(): 삭제할 요소의 인덱스를 통해 삭제합니다.
3. clear(): 리스트 내부 요소 전체 삭제
'''
points = [88, 99, 56, 92, 100, 78]

points.remove(92)
print(points)

del(points[2])
print(points)

points.clear()
print(points)

pokemon = ['피카츄', '라이츄', '파이리', '꼬부기', '버터풀']

'''
삭제할 이름을 입력받아서 그에 해당하는 이름을 실제로 리스트에서 삭제한 후
삭제 후 정보를 출력하세요.

- remove()와 del()을 이용하여 각각 출력해보세요.
'''
print('-' * 40)

print(pokemon)
your_pokemon = input('삭제할 포켓몬을 입력하세요: ')

#remove
pokemon.remove(your_pokemon)
print(pokemon)

#del
your_pokemon = input('삭제할 포켓몬을 입력하세요: ')

idx = -1

for i in range(0, len(pokemon)):
    if pokemon[i] == your_pokemon:
        idx = i
        break

if idx != -1:
    del(pokemon[idx])
    print(pokemon)
else:
    print('해당되는 포켓몬이 없습니다.')
