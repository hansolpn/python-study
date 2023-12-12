'''
* 인수의 기본값

- 파이썬에서는 인수의 기본값을 설정하여, 자주 바뀌지 않는 
매개값은 기본값으로 처리할 수 있도록 해 줍니다.
'''

def cale_stepsum(begin, end, step = 1):
    sum = 0
    for n in range(begin, end + 1, step):
        sum += n
    return sum

print(cale_stepsum(1, 10, 1))
print(cale_stepsum(1, 10, 2))

# 기본값이 지정된 인수를 오른쪽으로 몰아 주서야 합니다
def calc_sum(end, begin = 0 , step = 1):
    sum = 0
    for n in range(begin, end + 1, step):
        sum += n
    return sum

print(calc_sum(100))

