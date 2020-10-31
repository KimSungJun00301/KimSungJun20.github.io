#연습문제
#구구단 출력하기(2~9단까지 모두 출력)
#2차원 반복문 이용
answer = 0
for i in range(2,10):
    for g in range(1,10):
        print("[i: %d, g: %d]" %(i,g))
        print("%d X %d=" %(i,g),i*g)
        
