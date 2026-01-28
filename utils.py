import os
import time

def clear_screen():
    """Limpa o terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def pause(message="\nPressione ENTER para continuar..."):
    input(message)


def slow_print(text, delay=0.03):
    """Imprime texto com efeito de digitação"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
