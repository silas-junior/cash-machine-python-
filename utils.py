import os


def clear_terminal():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)


def header(name='default'):
    print("****************************************")
    print("*** School of Net - Caixa Eletrônico ***")
    print("****************************************")

    if name != 'default':
        print("    Seja bem-vindo, " + name)
        print("****************************************")
        print("****************************************")