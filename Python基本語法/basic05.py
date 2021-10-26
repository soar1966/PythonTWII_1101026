import random
if __name__== '__main__':#主程式開始
    score = random.randint(0,100)# 0~100亂數
    if score >= 60 :
        print(score,'Pass')
    else:
        print(score,'Fail')
    print(score, 'Pass' if score>=60 else 'Fail')
    print(9//2)
    print(9 / 2)
    print(6/2*(1+2))
    x = True
    y = False
    z = False
    if x or y and z:
        print("yes")
    else:
        print("no")


