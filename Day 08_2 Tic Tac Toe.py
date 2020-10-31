# 0 0 0
# 0 0 0
# 0 0 0

#승리자를 알려면
#반복문 밖에서 승리자를 담는 변수 만들고
# winner = 0 변수 # 1:P1 승리 / 2:P2 승리

# check
# 가로검사 -> 가로완성이 존재한다: 해당 값의 주인 확인 -> 승리자 변수에 담음
# 세로검사
# 대각선 검사(왼오)
# 대각선 검사(오왼)

# 종료조건
# 반복문의 말미에서
# if winner == 1: P1이 이겼다 break
# if winner == 2: P2이 이겼다 break

#반복문을 돌때마다[] turn이 1씩 증가
# 플레이어의 입력값을 받기 직전에 turn 검사
# if turn %2 ==0: # player1 차례
# if turn %2 ==1: # player2 차례
# 목표: 리스트를 자유자재로 다룰 수 있다.
# map = [0,0,@,0,^,@,0,0,0]
map = [1,2,3,4,5,6,7,8,9]


turn = 0

winner = 0

while True:
    print("------TIC TAC TOE-------")

    for i in range(9):
        print(map[i],end=" ")
        if i % 3 == 2:
            print()

    if turn % 2 == 0:
        ply1 = int(input("번호 입력 \np1:"))
        if map[ply1-1] < 10:
            map[ply1-1] = '@'
            turn += 1
    print("----------TIC TAC TOE--------")
    
    for i in range(9):
        print(map[i],end=" ")
        if i % 3 == 2:
            print()
            
    if turn % 2 == 1:
        ply2 = int(input("번호 입력 \np2:"))
        if map[ply2-1] < 10:
            map [ply2-1] = '^'
            turn += 1

    if map[ply1] == '@':
        map

    
            

   
    #for i in range(9):
     #   if i == ply1:
     #       print('@',end ="")
     #   print("%d" %'@')
    
    #ply2 = int(input("번호 입력:"))
    #for i in range(9):
    #    if i == ply2:
    #        print('^')
    #    print("%d" %'^')


