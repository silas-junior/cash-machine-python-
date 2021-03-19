from file import open_file_bank, write_money_notes, write_bank_accounts
from utils import header


def main():
    header()
    make_money_notes('w')
    file = open_file_bank('a')
    file.write('\n')
    file.close()
    make_bank_accounts('a')


def make_money_notes(mode):
    file = open_file_bank(mode)
    write_money_notes(file)
    file.close()
    print('Cédulas gravadas com sucesso!')


def make_bank_accounts(mode):
    file = open_file_bank(mode)
    write_bank_accounts(file)
    file.close()
    print('Contas bancárias gravadas com sucesso!')


main()
