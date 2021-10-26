if __name__== '__main__':#主程式開始
    amount = 200 #雞加兔子 隻
    feet = 240 #  腳數量
    """
    假設 雞和和兔子都是兩隻腳 83*2 = 166
        兔子的腳數量  240-166 = 74
        兔子的數量    74/2 = 37
        雞的數量      83-37 = 46
    """
if amount * 2<= feet <= amount * 4: #限制範圍
    rabbit = (feet -amount * 2)/(4-2) #  腳數量
    chicken = amount -rabbit
    print('兔子 : ',rabbit," 雞 :",chicken)
else:
    print('amount :',amount , 'feet :',feet , '設定錯誤')



