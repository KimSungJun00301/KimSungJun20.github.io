db_id = 'bruno'
db_pw = 'monster415'

my_id = input('id:')



if db_id != my_id:
    print("try again")
elif db_id == my_id:
    my_pw = input('pw:')
    if db_pw != my_pw:
        print("try agin")
    elif db_pw == my_pw:
        print("login")

        보유현금 = n = 300000000
        입금현금 = m = 200000000


        menu = int(input("1)입금, 2)출금, 3)조회"))
        if menu ==1:
            print('보유현금은 증가합니다')
            cash = int(input("입금현금:"))
            입금현금 += 보유현금
            
            
        
