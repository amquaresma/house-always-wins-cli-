import random
from utils import clear_screen, pause, slow_print

def run():
    clear_screen()
    print("📊 LABORATÓRIO DE PROBABILIDADE")
    print("-" * 45)
    print("1 - Cara ou Coroa")
    print("2 - Dado (1 a 6)")
    print("0 - Voltar ao menu")

    option = input("\nEscolha uma opção: ").strip()

    if option == "0":
        return

    try:
        rounds = int(input("Quantas repetições deseja simular? "))
    except ValueError:
        print("Número inválido.")
        pause()
        return

    if rounds <= 0:
        print("Número inválido.")
        pause()
        return

    clear_screen()

    if option == "1":
        heads = 0
        tails = 0

        for _ in range(rounds):
            if random.choice(["H", "T"]) == "H":
                heads += 1
            else:
                tails += 1

        print("🪙 RESULTADO: CARA OU COROA")
        print(f"Total de jogadas: {rounds}")
        print(f"Caras: {heads} ({heads/rounds:.2%})")
        print(f"Coroas: {tails} ({tails/rounds:.2%})")

        slow_print(
            "\n📘 Teoricamente, a chance é 50% para cada lado.\n"
            "Quanto mais repetições, mais o resultado se aproxima da teoria."
        )

    elif option == "2":
        results = {i: 0 for i in range(1, 7)}

        for _ in range(rounds):
            roll = random.randint(1, 6)
            results[roll] += 1

        print("🎲 RESULTADO: DADO")
        print(f"Total de lançamentos: {rounds}\n")

        for number, count in results.items():
            print(f"{number}: {count} ({count/rounds:.2%})")

        slow_print(
            "\n📘 Cada número possui 1/6 (~16,67%) de chance.\n"
            "A simulação mostra como a probabilidade se distribui na prática."
        )

    else:
        print("Opção inválida.")

    pause("\nPressione ENTER para voltar ao menu...")
