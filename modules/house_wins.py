import random
from utils import clear_screen, pause, slow_print

def run():
    clear_screen()
    print("🧪 A CASA SEMPRE GANHA")
    print("-" * 45)

    try:
        players = int(input("Quantidade de jogadores simulados: "))
        rounds = int(input("Rodadas por jogador: "))
    except ValueError:
        print("Entrada inválida.")
        pause()
        return

    if players <= 0 or rounds <= 0:
        print("Valores inválidos.")
        pause()
        return

    casino_profit = 0
    winners = 0

    for _ in range(players):
        balance = 100

        for _ in range(rounds):
            bet = 10
            chance = random.random()

            if chance < 0.05:  # mesma lógica do slot
                balance += bet * 5
                casino_profit -= bet * 5
            else:
                balance -= bet
                casino_profit += bet

            if balance <= 0:
                break

        if balance > 100:
            winners += 1

    clear_screen()
    print("📊 RESULTADO DA SIMULAÇÃO")
    print("-" * 35)
    print(f"Jogadores simulados: {players}")
    print(f"Rodadas por jogador: {rounds}")
    print(f"Jogadores que lucraram: {winners}")
    print(f"Percentual de vencedores: {winners/players:.2%}")
    print(f"\n💰 Lucro total do cassino: R${casino_profit}")

    slow_print(
        "\n📘 Mesmo com alguns vencedores individuais,\n"
        "o resultado agregado favorece sempre o cassino.\n"
        "Isso ocorre por causa da vantagem estatística da casa."
    )

    pause("\nPressione ENTER para voltar ao menu...")
