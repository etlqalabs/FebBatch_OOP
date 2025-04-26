class BankAccount:
    def __init__(self,owner,balance,pin):
        self.owner = owner
        self._balance = balance
        self.__pin = pin

    def getPin(self):
        print(self.__pin)

class SavingsAccount(BankAccount):
    def __init__(self,owner,balance,pin,interest_rate):
        super().__init__(owner,balance,pin)
        self.interest_rate = interest_rate
    def print_inetrest_rate(self):
        print("Interest rate is",self.interest_rate)
'''
acc1 = SavingsAccount("Hetu",20000,1234,6.5)
print(acc1.owner)
print(acc1._balance)

acc1.print_inetrest_rate()
acc1.getPin()
# print(acc1.__pin)
'''


sa = BankAccount("Hetu",20000,1234)
print(sa._balance)
print(sa.__pin)
sa.getPin()