# import main
# import utils
#
# print(main.accounts_list)
# utils.clear_terminal()
# print(main.accounts_list)
import os
from cash_machine_variables import money_notes, accounts_list

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
        file.write(f"{note}={value};")


def write_bank_accounts(file):
    for account, info_account in accounts_list.items():
        file.writelines((
            account, ';',
            info_account['name'], ';',
            info_account['password'], ';',
            str(info_account['balance']), ';',
            str(info_account['admin']), ';',
            '\n'
        ))


def read_money_notes(file):
    line = file.readline()
    while line.find(';') != -1:
        semicolon_pos = line.find(';')
        note_block = line[0:semicolon_pos]
        set_note_block(note_block)
        if semicolon_pos + 1 == len(line):
            break
        else:
            line = line[semicolon_pos + 1:len(line)]


def read_bank_accounts(file):
    lines = file.readlines()
    lines = lines[1: len(lines)]
    for account_line in lines:
        extract_bank_account(account_line)
        

def extract_bank_account(account_line):
    account_data = []
    while account_line.find(';') != -1:
        semicolon_pos = account_line.find(';')
        data_block = account_line[0:semicolon_pos]
        account_data.append(data_block)
        if semicolon_pos + 1 == len(account_line):
            break
        else:
            account_line = account_line[semicolon_pos + 1:len(account_line)]
    add_bank_account(account_data)


def add_bank_account(account_data):
    accounts_list[account_data[0]] = {
        'name': account_data[1],
        'password': account_data[2],
        'balance': float(account_data[3]),
        'admin': True if account_data[4] == 'True' else False
    }


def set_note_block(note_block):
    equal_pos = note_block.find('=')
    note = note_block[0:equal_pos]
    count_position_block = len(note_block)
    notes_quantity = note_block[equal_pos + 1:count_position_block]
    print(note, notes_quantity)
    money_notes[note] = int(notes_quantity)


def load_bank_data():
    file = open_file_bank('r')
    read_money_notes(file)
    file.close()

    file = open_file_bank('r')
    read_bank_accounts(file)
    file.close()
