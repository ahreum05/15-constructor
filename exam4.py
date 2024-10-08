from random import random
from random import randint
from random import randrange
from random import sample

# 0<= 실수 <1.0
print(random())
print('-' * 20)

# 0~9 사이의 정수
print(randint(0, 9))
print('-' * 20)

# 5~10 사이의 정수
print(randrange(5, 10))
print('-' * 20)

# 임의의 문자
print(chr(randint(65, 90)))  # 'A'=65, 'Z'=90
print('-' * 20)

# 리스트에서 임의의 값 선택해서 추출하기
print(sample([1, 2, 3, 4, 5], 2))
# 로또 번호 1~45 사이의 숫자 6개
print(sorted(sample([a for a in range(1, 46)], 6)))


