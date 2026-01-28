import random
import time

def run():
    balance = 100.0
    rounds = 0
    wins = 0
    losses = 0

    print("\n🎭 ILUSÃO DO LUCRO")
    print("-" * 40)
    print("Você começa com R$100.")
    print("Ganhos pequenos são frequentes.")
    print("Perdas grandes acontecem raramente… mas doem.\n")

    while balance > 0 and rounds < 50:
        rounds += 1
        bet = min(10, balance)

        print(f"\nRodada {rounds} | Saldo atual: R${balance:.2f}")
        time.sleep(0.7)

        chance = random.random()

        if chance < 0.65:
            # vitória pequena
            gain = bet * 0.3
            balance += gain
            wins += 1
            print(f"✅ Você ganhou R${gain:.2f} (vitória pequena)")
        else:
            # perda grande
            loss = bet * 2
            balance -= loss
            losses += 1
            print(f"❌ Você perdeu R${loss:.2f} (perda grande)")

        time.sleep(0.6)

        if balance <= 0:
            print("\n💸 Seu saldo zerou.")
            break

    print("\n📊 RESULTADO FINAL")
    print("-" * 30)
    print(f"Rodadas jogadas: {rounds}")
    print(f"Vitórias pequenas: {wins}")
    print(f"Derrotas grandes: {losses}")
    print(f"Saldo final: R${balance:.2f}")

    print("\n🧠 REFLEXÃO:")
    print(
        "Cassinos usam vitórias frequentes e pequenas\n"
        "para criar a sensação de progresso.\n"
        "Mas poucas perdas grandes anulam tudo.\n"
        "Isso é a ILUSÃO DO LUCRO."
    )
