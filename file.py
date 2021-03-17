# import main
# import utils
#
# print(main.accounts_list)
# utils.clear_terminal()
# print(main.accounts_list)
import os
from cash_machine_variables import accounts_list

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH + '/file_test.dat', 'w')
file = open(BASE_PATH + '/file_test.dat', 'w')

for key, account in accounts_list.items():

    file.write(f"Nome: {account['name']}\nSaldo: R$ {account['balance']},00\n\n")

file.close()
