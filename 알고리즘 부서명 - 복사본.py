# 문제1)
data1 = [{"부서" : "영업부", "직원명단" : ["aaa","bbb","ccc"]},
         {"부서" : "사업부", "직원명단" : ["ddd","eee","fff"]},
         {"부서" : "마케팅부", "직원명단" : ["ggg","ggg","iii"]},
         {"부서" : "총무부", "직원명단" : ["jjj","kkk","lll"]}
         ]

for i in data1:
   print(i)

a = input("부서명을 입력하세요 :")

for i in data1:
   if i ["부서"] == a:
      print(i["직원명단"])

# 문제2)
# 아래의 데이터는 각직원별 올해의 금여 내역
# 이름을 입력하면 급여 총액 출력 aaa ==> 120
data2 = [{"이름" : "aaa" , "급여" : [10,10,10,10,10,10,10,10,10,10,10,10]},
         {"이름" : "bbb" , "급여" : [20,20,20,20,20,20,20,20,20,20,20,20]},
         {"이름" : "ddd" , "급여" : [30,30,30,30,30,30,30,30,30,30,30,30]},
         {"이름" : "eee" , "급여" : [40,40,40,40,40,40,40,40,40,40,40,40]},
         {"이름" : "ggg" , "급여" : [50,50,50,50,50,50,50,50,50,50,50,50]},
         {"이름" : "hhh" , "급여" : [60,60,60,60,60,60,60,60,60,60,60,60]}]
for i in data2:
    print(i["급여"])
    
a = "bbb"
total = 0
for i in data2:  
    if i["이름"] == a:
        for n in i["급여"]:
            total += n
print(total)


