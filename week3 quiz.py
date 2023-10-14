# 환율표 딕셔너리 생성
exchange_rates = {
    "달러": 1320,  # 1달러 당 원화 환율
    "엔": 950,     # 1엔화 당 원화 환율
    "위안": 182     # 1위안화 당 원화 환율
}

# 철수가 가진 돈을 리스트 요소로 하는 리스트 변수 생성
Money = [13, 200, 13]  # 각각 달러, 엔화, 위안

# 딕셔너리의 Key 값을 리스트로 가져오기
currencies = list(exchange_rates.keys())

# 통화의 원화 계산과 리스트 슬라이싱을 사용한 계산
krw_values = [Money[i] * exchange_rates[currency] for i, currency in enumerate(currencies)]

# 결과 출력
total_krw = sum(krw_values)
print(f"철수가 가지고 있는 돈의 원화 가치는 {total_krw}원 입니다.")
