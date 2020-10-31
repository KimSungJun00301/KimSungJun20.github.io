#바나프레소 쌤 풀이

import random

price1 = 1500
price2 = 2500
price3 = 3000

cnt1 = 0
cnt2 = 0
cnt3 = 0

주문번호 = 0

n=0
while n < 5:                #  =  for i in range(5)
    print("1. 주문")
    sel = int(input("메뉴 선택:"))

    if sel == 1:
        주문번호 = random.randint(1000,9999)
        print("1. 아메리카노 1,500")
        print("2. 카푸치노 2,500")
        print("3. 카페라떼 3,000")         # 쌤 풀이에서만 변형
        
        pick = int(input("음료 선택:"))

        if pick == 1:
            cnt1 += 1
        if pick == 2:
            cnt2 += 1
        if pick == 3:
            cnt3 += 1
        if pick ==5:
            cnt4 += 1
        if pick == 6:
            cnt4 += 1
        if pick == 7:
            cnt4 += 1
        if pick == 8:
            cnt4 += 1
        if pick == 9:
            cnt4 += 1
        

    n += 1

total = cnt1 * price1 + cnt2 * price2 + cnt3 * price3
print("총 금액은 %d원입니다:" % total)
money = int(input("현금 입력:"))

if money >= total:
    print('''------------BANAPRESSO------------
주문번호를 확인해주세요.                     
주문번호''' , 주문번호)            #영수증 출력
    print("------------------------------------")
    if cnt1 != 0:
        print("아메리카노 %d개 \t %d원" %(cnt1, cnt1*price1))
    if cnt2 != 0:
        print("카푸치노 %d개 \t %d원" %(cnt2, cnt2*price2))
    if cnt3 != 0:
        print("카페라떼 %d개 \t %d원" %(cnt3, cnt3*price3))
    print("주문해주셔서 감사합니다.")
    print("total: %d원" %total)
    print("잔액: %d원:" %(money - total))
    print("-----------------------------------")
    
else:
    print("잔액이 부족합니다")
