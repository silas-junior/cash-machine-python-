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


def main():
    auth = False
    while not auth:
        header()

        account_typed = input('Digite sua conta: ')
        password_typed = getpass.getpass('Digite sua senha: ')

        if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
            auth = True
            selected_options = 0
            show_last_option = str
            admin = accounts_list[account_typed]['admin']

            clear()

            name = accounts_list[account_typed]['name']
            balance = accounts_list[account_typed]['balance']
            header(name)

            while auth:
                print("1 - Saldo")
                print("2 - Saque")
                print("3 - Sair")

                if admin:
                    print("4 - Incluir cédulas")

                option = input("Escolha uma das opções acima: ")

                if option == '1':
                    show_last_option = f"Seu saldo: R$ {balance},00"
                    selected_options += 1
                elif option == '2':
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

                        show_last_option = "Não foi possível realizar o saque. \nO caixa não tem cédulas disponíveis para este valor."

                        selected_options += 1
                    elif value == 0 and balance > int(value_typed):

                        show_last_option = f"Saldo: R$ {balance},00 \nVocê está sacando: R$ {value_typed},00 \nNa sua conta irá sobrar: R$ {rest},00 \nAguarde até que as notas sejam liberadas."
                        selected_options += 1

                    elif balance < int(value_typed):
                        show_last_option = f'Valor de saque maior que o valor em conta!\nVocê quer sacar R$ {value_typed},00 mas possui R$ {balance},00 em sua conta'
                        selected_options += 1

                elif option == '3':
                    auth = False
                    show_last_option = "Até logo!"
                elif option == '4' and admin:
                    amount = input('Digite a quantidade de cédulas: ')
                    note = input('Digite a cédula a ser inclúida: ')
                    selected_options += 1

                    if note not in money_notes:
                        print('Vocẽ quer inserir uma nota que não existe')
                        selected_options += 1
                    else:
                        money_notes[note] += int(amount)
                        show_last_option = f"Você inseriu {amount} notas de {note} reais"
                        print(money_notes)
                        selected_options += 1

                else:
                    show_last_option = "A opção que você escolheu não existe"
                    selected_options += 1

                if selected_options >= 1:
                    clear()
                    show_option(show_last_option)
                    selected_options = 0

        else:
            show_last_option = "Acesso negado. Verifique conta e senha"

        # input("Pressione <ENTER> para continuar...")

        clear()
        show_option(show_last_option)


def header(name='default'):
    print("****************************************")
    print("*** School of Net - Caixa Eletrônico ***")
    print("****************************************")

    if name != 'default':
        print("    Seja bem-vindo, " + name)
        print("****************************************")
        print("****************************************")


def clear():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)


def show_option(option_content):
    print("****************************************")
    print(option_content)
    print("****************************************")


main()
