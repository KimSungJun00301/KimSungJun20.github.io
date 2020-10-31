# 1)가위 2)바위 3)보

import random

com =0
me =0

win_com =0
win_me =0
draw=0

n=0            #초기식
while n < 11:  #조건식
    com = random.randint(1,3)
    me = int(input("1)가위, 2)바위, 3)보:"))
    if com ==1:
        print("컴퓨터: 가위")
    elif com == 2:
        print("컴퓨터: 바위")
    elif com ==3:
        print("컴퓨터: 보")
    if me ==1:
        print("나: 가위")
    elif me ==2:
        print("나: 바위")
    elif me ==3:
        print("나: 보")

    #승패 출력
    if com ==me:
        print("비겼다")
        draw =draw+1
    elif com ==1 and me ==2:
        print("내가 이겼다")
        win_me +=1
    elif com ==2 and me ==3:
        print("내가 이겼다")
        win_me +=1
    elif com ==3 and me ==1:
        print("내가 이겼다")
        win_me +=1
    elif me ==1 and com ==2:
        print("컴퓨터가 이겼다")
        win_com +=1
    elif me==2 and com ==3:
        print("컴퓨터가 이겼다")
        win_com +=1
    elif me ==3 and com ==1:
        print("컴퓨터가 이겼다")
        win_com +=1

    n +=1 #증감식

print("컴퓨터: %d, 나:%d, 비긴수: %d" %(win_com,win_me,draw))

if win_com == win_me:
    print("draw")
elif win_com >= win_me:
    print("컴퓨터가 이겼다")
elif win_me >= win_com:
    print("내가 이겼다")


        
