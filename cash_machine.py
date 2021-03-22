class BankAccount:
    def __init__(self, account_number, name, password, balance, admin):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.balance = balance
        self.admin = admin


accounts_list = {
    BankAccount('0001-01', 'Fulano da Silva', '123456', 500, False),
    BankAccount('0002-02', 'Ciclano Pereira', '654321', 757.86, False),
    BankAccount('2222-22', 'Admin Silva', '112233', 2960, True),
}