class CashMachineConsole:

    @staticmethod
    def call_operation():
        option_typed = CashMachineConsole.get_menu_options_typed()
        CashMachineOperation.do_operation(option_typed)

    @staticmethod
    def get_menu_options_typed():
        print("1 - Saldo")
        print("2 - Saque")
        return input("Escolha uma das opções acima: ")


class CashMachineOperation:

    @staticmethod
    def do_operation(option):
        if option == '1':
            ShowBalance.do_operation()
        elif option == '2':
            WithDraw.do_operation()


class ShowBalance:

    @staticmethod
    def do_operation():
        print('Mostrando o saldo...')


class WithDraw:

    @staticmethod
    def do_operation():
        print('Sacando dinheiro...')
