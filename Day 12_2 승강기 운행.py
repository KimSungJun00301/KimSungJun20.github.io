# 다차원 리스트

# 1)캐릭터 이동
# 2)승강기 제어 시스템
# 3) 사다리 게임

# abs(): 절대값을 반환해주는 함수



import random

elve1004 = [0]*15
elve1005 = [0]*15
elve1006 = [0]*15
ME = 5

EV1004 = random.randint(0,15)
EV1005 = random.randint(0,15)
EV1006 = random.randint(0,15)

while True:
     print("------- The Grand Budapest Hotel -------")
     print("===============")
     elve = [[0]*15 for i in range(3)]
     for i in range(3):
          for j in range(15):
               print(elve[i][j],end=" ")
          print()
     print()
     print("elve1004",end=" ")
     for i in range(len(elve1004)):
          if i == elve1004:
               print("@",end=" ")
          else:
               print(end="")
     print()
     print("1) 위로 갈까?")
     print("2) 아래로 갈까?")
     set = int(input("입력:"))

     elve1004[i] = elve

     if set == 1:
          if x == len(elve)-1:
               print("올라갈 수 없습니다.")
          else:
               elve[x] = 0
               x += 1
     elif set == 2:
          if x == 0:
               print("내려갈 수 없습니다.")
          else:
               elve[x] = 0
               x -= 1
     else:
          print("더 이상 갈 수 없습니다.")
