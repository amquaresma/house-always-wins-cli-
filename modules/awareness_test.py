from utils import clear_screen, pause, slow_print

def run():
    score = 0

    questions = [
        {
            "question": "Cassinos online dão lucro garantido ao jogador?",
            "options": ["1 - Sim", "2 - Não"],
            "answer": "2",
            "explanation": "Cassinos são projetados para lucrar no longo prazo."
        },
        {
            "question": "O que é RNG?",
            "options": [
                "1 - Um bônus promocional",
                "2 - Um algoritmo de sorte",
                "3 - Gerador de números aleatórios"
            ],
            "answer": "3",
            "explanation": "RNG significa Random Number Generator."
        },
        {
            "question": "Ganhos iniciais significam lucro futuro?",
            "options": ["1 - Sim", "2 - Não"],
            "answer": "2",
            "explanation": "Ganhos iniciais fazem parte da ilusão psicológica."
        }
    ]

    for q in questions:
        clear_screen()
        print("🧠 TESTE DE CONSCIÊNCIA SOBRE APOSTAS")
        print("-" * 45)
        print(q["question"])
        print()

        for opt in q["options"]:
            print(opt)

        choice = input("\nSua resposta: ").strip()

        if choice == q["answer"]:
            score += 1
            print("\n✅ Resposta correta!")
        else:
            print("\n❌ Resposta incorreta.")

        slow_print(f"📘 {q['explanation']}")
        pause()

    clear_screen()
    print("📊 RESULTADO FINAL")
    print("-" * 30)

    if score == len(questions):
        slow_print(
            "Excelente!\n"
            "Você demonstra consciência sobre os riscos dos jogos de azar."
        )
    elif score >= len(questions) // 2:
        slow_print(
            "Atenção!\n"
            "Você possui algum conhecimento, mas ainda corre riscos."
        )
    else:
        slow_print(
            "Alerta!\n"
            "Baixa consciência sobre apostas. Informação é proteção."
        )

    pause("\nPressione ENTER para voltar ao menu...")
