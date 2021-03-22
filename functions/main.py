from file import load_bank_data
from utils import header, clear_terminal
from operations import login, menu_options, exec_option, show_message
from cash_machine_variables import accounts_list, money_notes


def main():
    while True:
        load_bank_data()
        header()

        account = login()

        if account:
            clear_terminal()
            message = str
            admin = accounts_list[account]['admin']
            name = accounts_list[account]['name']
            balance = accounts_list[account]['balance']

            header(name)

            while account:
                option_typed = menu_options(account)

                exec_option(option_typed, balance, admin)
        else:
            clear_terminal()
            message = "Acesso negado. Verifique conta e senha"
            show_message(message)

        clear_terminal()
        show_message(message)


main()
