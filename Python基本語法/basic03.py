import math
if __name__== '__main__':#主程式開始
    '''
    股票交易成本計算
    小明在股價 10 元時買了 Hero 公司股票 10 張，於 11 元全數賣出，
    請問小明賺了多少？
    提示：
    1張 = 1000股
    交易成本(台股)
    手續費：股票價值 * 1.425(‰) 買賣股票時都要扣除(不足 20 元者以 20 元計算。)
    證交稅：股票價值 * 3(‰) 賣出股票時才扣除
    '''
    amount  =1  #買進張數
    cost = 10 * amount * 1000 #買進成本
    fee_buy = cost * 0.001425 #買進手續費
    #fee_buy = math.floor(fee_buy)#小數點無條件捨去
    #fee_buy =int(fee_buy)#小數點無條件捨去
    #fee_buy = math.ceil(fee_buy)  # 小數點無條件進入
    fee_buy = round(fee_buy)  # 小數點4捨5入
    fee_buy = 20 if fee_buy < 20 else fee_buy #不足 20 元者以 20 元計算
    cost_add_free_buy = cost + fee_buy #買進總成本=買進成本+ 買進手續費
    print(cost,fee_buy,cost_add_free_buy)
    #========================================
    price = 11 * amount * 1000 #賣出金額
    free_sell = math.floor(price * 0.00142) #賣出手續費 無條件捨去
    free_sell = 20 if free_sell < 20 else free_sell  # 不足 20 元者以 20 元計算
    tax_sell = math.ceil(price * 0.003) #賣出證交稅 無條件進入
    price_sub_free_sell_tax_sell =price - free_sell -tax_sell
    print(price , free_sell , tax_sell , price_sub_free_sell_tax_sell )
    # ========================================
    profit = price_sub_free_sell_tax_sell - cost_add_free_buy
    print( '獲得利益=' ,profit ,'少賺', ((price- cost) - profit) )
