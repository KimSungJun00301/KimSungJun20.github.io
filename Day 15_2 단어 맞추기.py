import random

words = ["java","mysqi","jsp","spring","python"]

# shuffle
for i in range(100):
     rnum = random.randint(0,len(words)-1)    # random 인덱스를 추출
     temp = words[0]                          # 기준하는 인덱스 고
     words[0] = words[rnum]                   # 값교체식이 문제 없이 작성되어야 함
     words[rnum] = temp
     
n=0

while n < len(words):
     print("문제:",words[n])
     r = random.randint(0,len(words[n])-1)
     for i in range(len(words[n])):
          if i == r:
               print(end="*")
          else:
               print(words[n][i],end="")
     print()
     
     my_answer = input("답안:")

     #check
     if my_answer == words[n]:
          print("정답")
     else:
          print("땡")
          continue
     n += 1
print("The End")
