# 클래스 정의
class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price

# 음료 객체 생성
coffee = Beverage("커피", 3000)
green_tea = Beverage("녹차", 2500)
ice_tea = Beverage("아이스티", 3000)

# input()을 통해 주문 받는 음료 입력
selected_beverage = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티): ")

# 입력이 올바르지 않을 경우를 대비, 메뉴에 없는 경우 "잘못된 음료를 선택하셨습니다" 출력
if selected_beverage not in ["커피", "녹차", "아이스티"]:
    print("잘못된 음료를 선택하셨습니다.")
else:
    quantity = int(input("수량을 입력하세요: "))  # 음료의 수량 입력

    # 선택된 음료에 따라 객체 선택하여 calculate 함수 호출
    if selected_beverage == "커피":
        total_price = coffee.calculate(quantity)
    elif selected_beverage == "녹차":
        total_price = green_tea.calculate(quantity)
    elif selected_beverage == "아이스티":
        total_price = ice_tea.calculate(quantity)

# 최종 결괏값 출력
    print(f"{selected_beverage} {quantity}잔을 주문하셨습니다. 총 가격은 {total_price}원 입니다.")
