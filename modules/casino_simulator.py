import random
from utils import clear_screen, pause, slow_print

def run():
    balance = 100

    while True:
        clear_screen()
        print("🎰 SIMULADOR DE SLOT MACHINE (EDUCACIONAL)")
        print("-" * 45)
        print(f"Saldo atual: R${balance}")
        print("\n1 - Girar slot")
        print("0 - Voltar ao menu")

        option = input("\nEscolha uma opção: ").strip()

        if option == "0":
            break

        if option != "1":
            print("Opção inválida.")
            pause()
            continue

        try:
            bet = int(input("Digite o valor da aposta: "))
        except ValueError:
            print("Valor inválido.")
            pause()
            continue

        if bet <= 0 or bet > balance:
            print("Aposta inválida.")
            pause()
            continue

        # ALGORITMO DO SLOT (probabilidades reais)
        chance = random.random()

        if chance < 0.05:  # 5% de chance de ganho alto
            win = bet * 5
            balance += win
            result = f"🎉 Você ganhou R${win}!"
        else:
            balance -= bet
            result = f"❌ Você perdeu R${bet}."

        clear_screen()
        print(result)
        print("\n📊 EXPLICAÇÃO EDUCACIONAL:")
        slow_print(
            "Este jogo utiliza um gerador de números aleatórios (RNG).\n"
            "Apesar de ganhos ocasionais, a probabilidade favorece a casa.\n"
            "No longo prazo, a expectativa matemática é negativa para o jogador."
        )

        if balance <= 0:
            print("\n💀 Saldo zerado.")
            slow_print(
                "Este é um exemplo claro de como, mesmo com ganhos iniciais,\n"
                "o jogador tende a perder todo o saldo com o tempo."
            )
            pause()
            break

        pause()
