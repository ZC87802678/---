#奖金计算
def reward(profit):
    reward = 0.0
    if profit<=10:
        return profit*0.1
    elif profit<=20 and profit>10:
        return (profit-10)*0.075+1
    elif profit<=40 and profit>20:
        return (profit-20)*0.05+10*0.1+10*0.075
    elif profit<=60 and profit>40:
        return (profit-40)*0.03+20*0.05+10*0.075+10*0.1
    elif profit<=100 and profit>60:
        return (profit-60)*0.015+20*0.03+20*0.05+10*0.075+10*0.1
    elif profit>100:
        return (profit-100)*0.01+40*0.015+20*0.03+20*0.05+10*0.075+10*0.116
if __name__ == "__main__":
    profit = float(input("请输入当月利润： "))
    print( reward(profit)*10000)