from cash_machine_variables import accounts_list, money_notes
import getpass
from utils import clear_terminal


def login():
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    if account_typed in accounts_list and password_typed == \
            accounts_list[account_typed]['password']:
        return account_typed
    else:
        return False


def menu_options(account):
    print("1 - Saldo")
    print("2 - Saque")
    # print("3 - Sair")

    if accounts_list[account]['admin']:
        print("3 - Incluir cédulas")

    return input("Escolha uma das opções acima: ")


def exec_option(option_typed, balance, admin):
    if option_typed == '1':
        clear_terminal()
        message = f"Seu saldo: R$ {balance},00"
        show_message(message)

    elif option_typed == '2':
        withdrawal(balance)

    # elif option_typed == '3':
    #     clear_terminal()
    #     message = "Até logo!"
    #     show_message(message)

    elif option_typed == '3' and admin:
        include_notes()
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


def increment_options():
    selected_options = 0
    return selected_options + 1


# UNUSED
# def logout():
#     auth = False
#     return auth


def include_notes():
    amount = input('Digite a quantidade de cédulas: ')
    note = input('Digite a cédula a ser inclúida: ')
    increment_options()

    if note not in money_notes:
        clear_terminal()
        message = 'Vocẽ quer inserir uma nota que não existe!'
        show_message(message)
        increment_options()
    else:
        money_notes[note] += int(amount)
        clear_terminal()
        message = f"Você inseriu {amount} notas de {note} reais"
        show_message(message)
        increment_options()


def show_message(message):
    print("****************************************")
    print(message)
    print("****************************************")
