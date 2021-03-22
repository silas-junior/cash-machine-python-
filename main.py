from console import CashMachineConsole
from utils import clear_terminal, header


def main():
    clear_terminal()

    header()

    CashMachineConsole.call_operation()


if __name__ == '__main__':
    while True:
        main()

        input('Pressione <ENTER> para continuar...')