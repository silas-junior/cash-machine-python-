import getpass
import os

accountsList = {
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
moneyNotes = {
    '20': 5,
    '50': 5,
    '100': 5,
}


def main():
    auth = False
    while not auth:
        header()

        account_typed = input('Digite sua conta: ')
        password_typed = getpass.getpass('Digite sua senha: ')

        if account_typed in accountsList and password_typed == accountsList[account_typed]['password']:
            auth = True
            selectedOptions = 0
            showLastOption = str
            admin = accountsList[account_typed]['admin']

            os.system('cls' if os.name == 'nt' else 'clear')
            # if

            name = accountsList[account_typed]['name']
            balance = accountsList[account_typed]['balance']
            header(name)

            while auth:
                print("1 - Saldo")
                print("2 - Saque")
                print("3 - Sair")

                if admin:
                    print("4 - Incluir cédulas")

                option = input("Escolha uma das opções acima: ")

                if option == '1':
                    showLastOption = f"Seu saldo: R$ {balance},00"
                    selectedOptions += 1
                elif option == '2':
                    valueTyped = input('Digite o valor que você quer sacar: ')

                    moneyNotesUser = {}
                    value = int(valueTyped)

                    rest = balance - int(valueTyped)

                    if 0 < value // 100 <= moneyNotes['100']:
                        moneyNotesUser['100'] = value // 100
                        value = value - value // 100 * 100

                    if 0 < value // 50 <= moneyNotes['50']:
                        moneyNotesUser['50'] = value // 50
                        value = value - value // 50 * 50

                    if 0 < value // 20 <= moneyNotes['20']:
                        moneyNotesUser['20'] = value // 20
                        value = value - value // 20 * 20

                    if value != 0:
                        total = 0
                        for key, value in moneyNotes.items():
                            multi = int(key) * value
                            total += multi

                        showLastOption = "Não foi possível realizar o saque. \nO caixa não tem cédulas disponíveis para este valor."

                        selectedOptions += 1
                    elif value == 0 and balance > int(valueTyped):

                        showLastOption = f"Saldo: R$ {balance},00 \nVocê está sacando: R$ {valueTyped},00 \nNa sua conta irá sobrar: R$ {rest},00 \nAguarde até que as notas sejam liberadas."
                        selectedOptions += 1

                    else:
                        showLastOption = 'Valor de saque maior que o valor em conta!'
                        selectedOptions += 1

                elif option == '3':
                    auth = False
                    showLastOption = "Você encerrou a sessão!"
                elif option == '4' and admin:
                    amount = input('Digite a quantidade de cédulas: ')
                    note = input('Digite a cédula a ser inclúida: ')
                    selectedOptions += 1

                    if note not in moneyNotes:
                        print('Vocẽ quer inserir uma nota que não existe')
                        selectedOptions += 1
                    else:
                        moneyNotes[note] += int(amount)
                        showLastOption = f"Você inseriu {amount} notas de {note} reais"
                        print(moneyNotes)
                        selectedOptions += 1

                else:
                    showLastOption = "A opção que você escolheu não existe"
                    selectedOptions += 1

                if selectedOptions >= 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("****************************************")
                    print(showLastOption)
                    print("****************************************")
                    selectedOptions = 0

        else:
            showLastOption = "Acesso negado. Verifique conta e senha"

        # input("Pressione <ENTER> para continuar...")

        os.system('cls' if os.name == 'nt' else 'clear')
        print("****************************************")
        print(showLastOption)
        print("****************************************")


def header(name='default'):
    print("****************************************")
    print("*** School of Net - Caixa Eletrônico ***")
    print("****************************************")

    if name != 'default':
        print("    Seja bem-vindo, " + name)
        print("****************************************")
        print("****************************************")


main()

