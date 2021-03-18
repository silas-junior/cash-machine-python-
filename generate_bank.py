from file import open_file_bank, write_money_notes
from utils import header


def main():
    header()
    make_money_notes()


def make_money_notes():
    file = open_file_bank('w')
    write_money_notes(file)
    file.close()
    print('Cédulas gravadas com sucesso!')


main()
