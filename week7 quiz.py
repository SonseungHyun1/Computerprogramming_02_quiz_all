class fishbread:      # 붕어빵 클래스 생성
    total_sales=0     # 클래스 변수를 생성해 총 판매금액을 저장

# 생성자 메서드
# 객체의 초기 상태를 설정
    def __init__(self,종류,가격):
        self.종류=종류
        self.가격=int(가격)       # int(가격)을 사용했지만 아래 객체 생성에서 가격을 숫자형을 넣었다면 int를 제외

# 판매 메서드
# 붕어빵을 판매하는 동작
    def sell(self):
        print(f"{self.종류} 붕어빵이 {self.가격}원에 판매되었습니다")
        fishbread.total_sales += self.가격    # 총 판매 금액 합산
# 호출 될 때 마다 어떤 붕어빵이 얼마에 팔렸는지와 총 판매 금액을 합산해 출력

# 먹기 메서드
# 붕어빵을 먹는 동작
    def eat(self):
        print(f"{self.종류} 붕어빵을 먹었습니다.")
# 호출 될 때 마다 어떤 붕어빵을 먹었는지 출력

# 객체 생성
대왕_붕어빵= fishbread ("대왕","8000")
팥_붕어빵= fishbread ("팥","500")
슈크림_붕어빵= fishbread ("슈크림","800")
피자_붕어빵= fishbread ("피자","1500")
아이스크림_붕어빵= fishbread ("아이스크림","3500")

# 붕어빵 sell함수 호출
대왕_붕어빵.sell()
팥_붕어빵.sell()
슈크림_붕어빵.sell()
피자_붕어빵.sell()
아이스크림_붕어빵.sell()


print(f"총 판매금은 {fishbread.total_sales}원 입니다.")     # fishbread.total_sales 변수를 출력시켜 총 판매금액 명시
# 위치에 따라 어디에 출력 되는지 결정 / 위의 메서드 뒤에 위치하면 각 붕어빵이 팔릴 때 마다 총 판매 금액을 출력

print("---------------------------")  #sell과 eat 출력값 구분

# 붕어빵 eat함수 호출
대왕_붕어빵.eat()
팥_붕어빵.eat()
슈크림_붕어빵.eat()
피자_붕어빵.eat()
아이스크림_붕어빵.eat()


