class TotalMoney:

    def __init__(self, money):
        self.money = money

    def tax(self):
        calculation = round(self.money * 1.08)
        print("It is " + str(calculation) + "yen including tax.")


total_fee = int(input("Please input total money."))
total_money = TotalMoney(total_fee)
total_money.tax()
