#실습예제: 반복문 & 조건문
#->지하철 요금계산

# 1. 이용할 정거장 수를 입력받는다.
# 2. 다음과 같이 정거장 수에 따라 요금이 정산된다.
# 3. 요금표
# 1) 1~5: 500원
# 2) 6~10: 600원
# 3) 11~12: 650원
# 4) 13~14: 700원
# 5) 15~16: 750원
#...
#4. 보유현금을 입력받아 잔액까지 출력


subway=0

subway = int(input("이용할 정거장 수:"))

cash=0
if subway <= 5:
    print("cash:",500)
elif subway >= 6:
    subway = 600

cash=0        
while 1 <= subway <= 5:
    print("지하철 요금:", cash)
    if 6 <= subway <= 10:
        print("지하펄 요금:", cash)
    elif 11 <= subway:
        if subway += 1:
            subway += 50
        
