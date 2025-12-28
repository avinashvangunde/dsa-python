class Bank:
    def __init__(self,bal,acc):
        self.bal = bal
        self.acc = acc

    def debit(self,amount):
        self.bal -= amount
        print("curr bal --> ",self.bal)

    def credit(self,amount):
        self.bal+= amount
        print("curr bal --> ",self.bal)

    def getBal(self):
        return self.bal
    
ac1 = Bank(1200,123)
print(ac1.bal)
print(ac1.acc)
ac1.debit(200)
ac1.credit(500)
print(ac1.getBal())

