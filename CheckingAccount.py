class CheckingAccount:
    def __init__(self, name, address, account_number, balance):
        self.name = name
        self.address = address
        self.account_number = account_number
        self.__balance = balance

    def debit(self, amount):
        self.__balance = self.__balance - amount

    def credit(self, amount):
        self.__balance = self.__balance + amount

    def get_balance(self):
        return self.__balance


def main():
    account = CheckingAccount("Kevin Sherrell", "address", 123456, 2000000)
#     Get Account Balance
    print(account.get_balance())
#     Credit account by 3000000
    account.credit(3000000)
    print(account.get_balance())
#     Debit account by 5000
    account.debit(5000)
    print(account.get_balance())


main()
