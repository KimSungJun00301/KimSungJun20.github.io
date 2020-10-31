import random

ladder =[
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]
        ]

while True:
     #reset
     ladder[0] = [0]*5
     ladder[len(ladder)-1] =[0]*5
     STONE = 7
     x = random.randint(0,4)
     y= 0
     ladder[y][x] = STONE

     #print1
     print("S A D A R I")
     for yy in range(len(ladder)):
          for xx in range(len(ladder[yy])):
               if ladder[yy][xx] == STONE:
                    print('#',end=" ")
               elif ladder[yy][xx] == 0:
                    print("┃  ",end=" ")
               elif ladder[yy][xx] == 1:
                    if xx < 4 and ladder[yy][xx+1]==1:
                         print("┣━",end=" ")
                    elif xx > 0 and ladder[yy][xx-1] == 1:
                         print("┫  ",end=" ")
          print()
     print()
     set = int(input("1.출발 \n2. 종료 \n메뉴선택:"))

     if set == 1:
          #move:
          for yy in range(len(ladder)):
               if ladder[yy][x] == 1:        # 다음 행에서 값이 1이면,
                    # check
                    if x > 0 and ladder[yy][x-1] == 1: # 왼쪽이 1 (x움직일 방향 결정)
                         x -=1
                    elif x<4 and ladder [yy][x+1] == 1: # 오른쪾이 1
                         x += 1
                    elif ladder [yy][x] == 0:
                         pass

          #result
          print("[end idx: %d]"%x)
          ladder[len(ladder)-1][x] = STONE

          #print2
          print("S A D A R I")
          for yy in range(len(ladder)):
               for xx in range(len(ladder[yy])):
                    if ladder[yy][xx] == STONE:
                         print('#',end=" ")
                    elif ladder[yy][xx] == 0:
                         print("┃  ",end=" ")
                    elif ladder[yy][xx] == 1:
                         if xx < 4 and ladder[yy][xx+1]==1:
                              print("┣━",end=" ")
                         elif xx > 0 and ladder[yy][xx-1] == 1:
                              print("┫  ",end=" ")
               print()
          print()

     elif set == 2:
          break
          


     

          
