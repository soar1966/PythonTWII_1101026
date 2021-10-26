if __name__== '__main__':#主程式開始
    print(__name__)
    h=170
    w=60.0
    print(h,w)
    print(type(h),type(w)) #印出型別
    print('bmi=',w/(h/100)**2)
    #print('bmi='+ w / (h / 100) ** 2)
    print('bmi= ' +str( w / (h / 100) ** 2))#浮點數 轉 字串
    print('bmi=%.2f' % (w / (h / 100) ** 2) ) # 只取小數點兩位數字
    bmi = w/((h/100)**2)
    print('bmi={}'.format(bmi))
    print(f'bmi={bmi}')
    print('bmi={:.2n}'.format(bmi))#取兩位數
    print('bmi={:.4f}'.format(bmi))#取小數點4位數