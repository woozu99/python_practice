
def add(n1, n2):
    return n1 + n2

def add(n1, n2, n3):
    return n1 + n2 + n3

'''
* 위치 가변 인수

- 함수를 호출할 때는 함수 정의시에 지정한 인수의 개수만큼
값을 전달해야 합니다.

- 하지만 가변 인수를 사용하면 하나의 인수로 여러개의 값을
받아서 처리할 수 있습니다.

- 위치 가변인수는 함수 정의부에서 인수를 선언할 때
인수 앞에 * 기호를 붙여 선언하며, 이런 경우에 여러 개의
데이터를 튜플로 묶어서 함수 내부로 전달합니다.
'''

def calc_total(*nums):
    # print(type(nums)) -> type: tuple
    sum = 0
    for n in nums:
        sum += n
    return sum

print(calc_total(5,7,9,11,100,200,354,44, 25, 11, 67))

def calc_points(*points, name):
    print(f'{name} 학생의 성적 계산...')

    total = 0
    for p in points:
        total += p
    return total / len(points)

print('-' * 40)
# 가변인수와 일반 인수를 동시에 사용하실 때는
# 일반 인수를 반드시 키워드 인수 방식으로 전달하셔야 합니다.
result = calc_points(97, 100, 80, 100, 55, 60, name='김철수')
print(f'평균: {result}점')


'''
* 연습 - n개의 정수를 전달받아 가장 큰 숫자를 찾아서
 리턴하는 함수를 작성 하세요. (get_max)
 사용자에게 map()를 사용해서 여러 개의 값을 하나의 input()으로
 입력 받은 후 get_max()에게 전달해서 가장 큰 값을 리턴받으세요.
 입력받을 값은 5개로 하겠습니다.
'''
def get_max(*nums):
    max = nums[0]

    for n in nums:
        if n > max:
            max = n
    
    return max

n1, n2, n3, n4, n5 = map(int, input('정수 다섯개: ').split())

print('최대값:',get_max(n1,n2,n3,n4,n5))


