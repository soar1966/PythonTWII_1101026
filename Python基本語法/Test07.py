if __name__== '__main__':#主程式開始
    x = True
    y = False
    z = False
    if not x or y:
        print(1)
    elif not x or not y and z:
        print(2)
    elif not x or y or not y and x:
        print(3)
    else:
        print(4)
    print("not x or y:=>",not x or y)
    print("not x or not y and z:=>", not x or not y and z)
    print("not x or y or not y and x:=>", not x or y or not y and x)
