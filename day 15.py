import random

names = ['사과','강아지','그림자','복권','구름']
start = names[random.randint(0,5)] ## 제시어 -> 사용자 키워드

p1=1
p2=2

play = 0

print("----------- 끝말잇기 게임 -------------")
print(start,"->")

run = True

while run:
     new = "" ## 사용자 키워드 신규입력
     if play % 2 == 0:
          new = input("p1:")
     elif play % 2 == 1:
          new = input("p2:")

     #check
     #check = 1(필요있짆 않음)
     if start[len(start)-1] != new[0]: # 사(과) = new 변수의 0인덱스
          if play % 2 == 0:
               print("p2가 이겼다")
          else:
               print("p1가 이겼다")
          print("Game Over!!")
          break
     else:
          start = new     # 위 구조 반복
          play += 1

print("-----------------------")
