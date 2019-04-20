class Totalmoney:

    def __init__(self, money):
        self.money = money

    def tax(self):
        # Tax Calculation
        calculation = round(self.money * 1.08)
        print("税込金額は" + str(calculation) + "円です。")


total_fee = int(input("合計金額を入力してください"))
total_money = Totalmoney(total_fee)
total_money.tax()
