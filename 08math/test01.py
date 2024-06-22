class money:
    def __init__(self, inputdata):
        self.restMoney = int(inputdata)
        self.quarter = 0
        self.dime = 0
        self.nickel = 0
        self.penny = 0

numOfTry = int(input())
moneys = []
for _ in range(0,numOfTry):
    moneys.append(money(input()))

def moneyToChange(moneys):
    for money in moneys:
        if money.restMoney//25 > 0:
            money.quarter = money.restMoney // 25
            money.restMoney -= money.quarter * 25
        if money.restMoney//10 > 0:
            money.dime = money.restMoney // 10
            money.restMoney -= money.dime * 10
        if money.restMoney//5 > 0:
            money.nickel = money.restMoney // 5
            money.restMoney -= money.nickel * 5
        if money.restMoney> 0:
            money.penny = money.restMoney
            money.restMoney -= money.penny

moneyToChange(moneys)

for i in range(0, numOfTry):
    print(moneys[i].quarter, moneys[i].dime, moneys[i].nickel, moneys[i].penny)