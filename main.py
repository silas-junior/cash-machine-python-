from utils import header, clear_terminal
from operations import login, menu_options, exec_option, show_message
from cash_machine_variables import accounts_list


def main():
    auth = False
    while not auth:
        header()

        account = login()

        if account:
            clear_terminal()
            auth = True
            message = str
            admin = accounts_list[account]['admin']
            name = accounts_list[account]['name']
            balance = accounts_list[account]['balance']

            header(name)

            while auth:
                option_typed = menu_options(account)

                exec_option(option_typed, account, balance, admin, auth)
        else:
            clear_terminal()
            message = "Acesso negado. Verifique conta e senha"
            show_message(message)

        clear_terminal()
        show_message(message)


main()
