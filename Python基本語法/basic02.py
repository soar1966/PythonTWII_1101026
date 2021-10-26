import math
if __name__== '__main__':#主程式開始
    r=123
    #求出 圓面積 & 球體積(利用 math api取的圓周率)
    area = math.pow(r,2)*math.pi #圓面積 r*r*3.14
    print('圓面積=%.2f' % area)
    volume = 4/3 * math.pow(r,3)*math.pi #球體積 4/3 r*r*r*3.14
    print('球體積=%.2f' % volume)
    print('球體積={:,.2f}'.format(volume) )# 千分位
    # 千分位
    print(area,type(area))
    print('%.2f'% area)
    print(format(float('%.2f' % area),","))
