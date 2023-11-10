import random

def lucky_lotto_number():
    lotto_numbers = random.sample(range(1, 46), 6)
    lotto_numbers.sort()
    result = f"생성된 로또 번호는 {lotto_numbers}입니다."
    return lotto_numbers, result

lotto_numbers, results = lucky_lotto_number()
print(results)









