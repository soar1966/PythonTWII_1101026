def getRabbitAndChicken(amount , feet):
    rabbit = (feet - amount * 2) / (4 - 2)  # 腳數量
    chicken = amount - rabbit
    return rabbit,chicken

if __name__== '__main__':#主程式開始
    ra,ch = getRabbitAndChicken(83 , 240)
    print(ra,ch)
