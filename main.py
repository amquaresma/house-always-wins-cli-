from menu import show_menu

def main():
    while True:
        option = show_menu()

        if option == "1":
            from modules.casino_simulator import run
            run()

        elif option == "2":
            from modules.awareness_test import run
            run()

        elif option == "3":
            from modules.probability_lab import run
            run()

        elif option == "4":
            from modules.profit_illusion import run
            run()

        elif option == "5":
            from modules.house_wins import run
            run()

        elif option == "0":
            print("\nPrograma encerrado. Obrigado por participar.")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
