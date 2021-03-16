import utils
from operations import login, menu_options, exec_option, show_message

accounts_list = {
    '0001-01': {
        'password': '123456',
        'name': 'Fulano da Silva',
        'balance': 500,
        'admin': False,
    },
    '0002-02': {
        'password': '654321',
        'name': 'Ciclano Pereira',
        'balance': 757.86,
        'admin': False,
    },
    '2222-22': {
        'password': '112233',
        'name': 'Admin Silva',
        'balance': 2960,
        'admin': True,
    },
}
money_notes = {
    '20': 5,
    '50': 5,
    '100': 6,
}


def main():
    auth = False
    while not auth:
        utils.header()

        account = login()

        if account:
            utils.clear_terminal()
            auth = True
            message = str
            admin = accounts_list[account]['admin']
            name = accounts_list[account]['name']
            balance = accounts_list[account]['balance']

            utils.header(name)

            while auth:
                option_typed = menu_options(account)

                exec_option(option_typed, account, balance, admin, auth)
        else:
            utils.clear_terminal()
            message = "Acesso negado. Verifique conta e senha"
            show_message(message)

        utils.clear_terminal()
        show_message(message)


main()
