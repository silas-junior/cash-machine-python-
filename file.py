# import main
# import utils
#
# print(main.accounts_list)
# utils.clear_terminal()
# print(main.accounts_list)
import os
from cash_machine_variables import money_notes

# from cash_machine_variables import accounts_list
#
#
# def write():
#     BASE_PATH = os.path.dirname(os.path.abspath(__file__))
#     print("Escrito")
#     file = open(BASE_PATH + '/file_test.dat', 'w')
#
#     for key, account in accounts_list.items():
#         file.write(f"Nome: {account['name']}\nSaldo: R$ {account['balance']},00\n\n")
#
#     file.close()
#
#
# def read():

#     file = open(BASE_PATH + '/file_test.dat', 'r')
#     print(file.read()) # Lê o arquivo inteiro
#     print(file.readline()) # Lê o linha por linha do arquivo
#     file.close()
#
#
# write()
# read()
BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def open_file_bank(mode):
    return open(BASE_PATH + '/_bank_file.dat', mode)


def write_money_notes(file):
    for note, value in money_notes.items():
        file.write(f"{note} = {value};")
