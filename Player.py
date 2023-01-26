class Player:
    
    def __init__(self, name, age, totalMoney):
        self.name = name
        self.age = age
        self.totalMoney = totalMoney

    def make_bet(self, betAmount):
        self.totalMoney -= betAmount

    def win_bet(self, winnings):
        self.totalMoney += winnings

