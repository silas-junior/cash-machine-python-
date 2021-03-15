import getpass
import os

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


# selected_options = 0


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

                # if option_typed == '1':
                #     show_balance()
                # elif option_typed == '2':
                #     value_typed = input('Digite o valor que você quer sacar: ')
                #
                #     money_notes_user = {}
                #     value = int(value_typed)
                #
                #     rest = balance - int(value_typed)
                #
                #     if 0 < value // 100 <= money_notes['100']:
                #         money_notes_user['100'] = value // 100
                #         value = value - value // 100 * 100
                #
                #     if 0 < value // 50 <= money_notes['50']:
                #         money_notes_user['50'] = value // 50
                #         value = value - value // 50 * 50
                #
                #     if 0 < value // 20 <= money_notes['20']:
                #         money_notes_user['20'] = value // 20
                #         value = value - value // 20 * 20
                #
                #     if value != 0:
                #         total = 0
                #         for key, value in money_notes.items():
                #             multi = int(key) * value
                #             total += multi
                #
                #         message = "Não foi possível realizar o saque. \nO caixa não tem cédulas disponíveis para este valor."
                #
                #         selected_options += 1
                #     elif value == 0 and balance > int(value_typed):
                #
                #         message = f"Saldo: R$ {balance},00 \nVocê está sacando: R$ {value_typed},00 \nNa sua conta irá sobrar: R$ {rest},00 \nAguarde até que as notas sejam liberadas."
                #         for note in money_notes_user:
                #             money_notes[note] -= money_notes_user[note]
                #         selected_options += 1
                #
                #     elif balance < int(value_typed):
                #         message = f'Valor de saque maior que o valor em conta!\nVocê quer sacar R$ {value_typed},00 mas possui R$ {balance},00 em sua conta'
                #         selected_options += 1
                #
                # elif option_typed == '3':
                #     auth = False
                #     message = "Até logo!"
                # elif option_typed == '4' and admin:
                #     amount = input('Digite a quantidade de cédulas: ')
                #     note = input('Digite a cédula a ser inclúida: ')
                #     selected_options += 1
                #
                #     if note not in money_notes:
                #         print('Vocẽ quer inserir uma nota que não existe')
                #         selected_options += 1
                #     else:
                #         money_notes[note] += int(amount)
                #         message = f"Você inseriu {amount} notas de {note} reais"
                #         print(money_notes)
                #         selected_options += 1

                # else:
                #     message = "A opção que você escolheu não existe"
                #     selected_options += 1

                # selected_options = increment_options()
                # if selected_options >= 1:
                #     clear()
                #     show_message(message)
                # selected_options = 0

        else:
            clear_terminal()
            message = "Acesso negado. Verifique conta e senha"
            show_message(message)

        clear_terminal()
        show_message(message)


def header(name='default'):
    print("****************************************")
    print("*** School of Net - Caixa Eletrônico ***")
    print("****************************************")

    if name != 'default':
        print("    Seja bem-vindo, " + name)
        print("****************************************")
        print("****************************************")


def increment_options():
    selected_options = 0
    return selected_options + 1


def exec_option(option_typed, account, balance, admin, auth):
    if option_typed == '1':
        clear_terminal()
        message = f"Seu saldo: R$ {balance},00"
        show_message(message)

    elif option_typed == '2':
        withdrawal(balance)

    elif option_typed == '3':
        clear_terminal()
        message = "Até logo!"
        show_message(message)

    elif option_typed == '4' and admin:
        include_notes()
        # selected_options += 1
    else:
        clear_terminal()
        message = "A opção que você escolheu não existe!"
        show_message(message)


def show_balance(balance):
    message = f"Seu saldo: R$ {balance},00"
    show_message(message)


def withdrawal(balance):
    value_typed = input('Digite o valor que você quer sacar: ')

    money_notes_user = {}
    value = int(value_typed)

    rest = balance - int(value_typed)

    if 0 < value // 100 <= money_notes['100']:
        money_notes_user['100'] = value // 100
        value = value - value // 100 * 100

    if 0 < value // 50 <= money_notes['50']:
        money_notes_user['50'] = value // 50
        value = value - value // 50 * 50

    if 0 < value // 20 <= money_notes['20']:
        money_notes_user['20'] = value // 20
        value = value - value // 20 * 20

    if value != 0:
        total = 0
        for key, value in money_notes.items():
            multi = int(key) * value
            total += multi

        clear_terminal()
        message = "Não foi possível realizar o saque. \nO caixa não tem cédulas disponíveis para este valor."
        show_message(message)

    elif value == 0 and balance > int(value_typed):
        clear_terminal()
        message = f"Saldo: R$ {balance},00 \nVocê está sacando: R$ {value_typed},00 \nNa sua conta irá sobrar: R$ {rest},00 \nAguarde até que as notas sejam liberadas."
        for note in money_notes_user:
            money_notes[note] -= money_notes_user[note]
        show_message(message)

    elif balance < int(value_typed):
        clear_terminal()
        message = f'Valor de saque maior que o valor em conta!\nVocê quer sacar R$ {value_typed},00 mas possui R$ {balance},00 em sua conta'
        show_message(message)


def logout():
    auth = False
    return auth


def include_notes():
    pass


def login():
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        return account_typed
    else:
        return False


def menu_options(account):
    print("1 - Saldo")
    print("2 - Saque")
    print("3 - Sair")

    if accounts_list[account]['admin']:
        print("4 - Incluir cédulas")

    return input("Escolha uma das opções acima: ")


def clear_terminal():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)


def show_message(message):
    print("****************************************")
    print(message)
    print("****************************************")


main()
