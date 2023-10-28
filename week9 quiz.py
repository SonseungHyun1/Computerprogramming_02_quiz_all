#Resident registration number (주민번호 유효성 판독기)

# 함수 선언
def validate_RRN(RRN):
    RRN = RRN.replace('-', '')      # '-' 제거

    # 주민번호 각 자리 계산
    result = int(RRN[0])*2 + int(RRN[1])*3 + int(RRN[2])*4 + int(RRN[3])*5 + int(RRN[4])*6 + int(RRN[5])*7 + \
             int(RRN[6])*8 + int(RRN[7])*9 + int(RRN[8])*2 + int(RRN[9])*3 + int(RRN[10])*4 + int(RRN[11])*5

    # 나머지 계산
    remainder = result % 11

    # 11에서 나머지를 뺀 값 계산
    result2 = (11 - remainder) % 10

    # 주민번호의 마지막 자리와 비교
    last_digit = int(RRN[-1])

    return result2 == last_digit

# 주민등록번호 입력 받기
주민번호_입력 = input("주민등록번호를 입력하세요 (예: 900101-1234567): ")

# 유효성 검사 결과 출력
if validate_RRN(주민번호_입력):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
