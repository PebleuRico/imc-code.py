import os
import time
os.system("cls")

def ligacao_para_amiga():
    print("📞 Discando para sua amiga...")
    time.sleep(2)
    print("🔊 *Atendeu!*")
    time.sleep(1)
    print("\nAmiga: Oii! Tudo bem? O que foi?")
    print("Você: Eai, vamo ver se você é brainrot de verdade? Quero que voce responda algumas perguntas:\n")

    # Pergunta 1
    resposta1 = (
        input("Pergunta 1: Quem é o ser mais lendário do Rizz supremo? (spoiler: Não é o mewing, ok?) ")
        .strip()
        .lower()
    )

    # Coloque a resposta correta aqui (exemplo: "skibidi" ou "mewing")
    if "skibidi" not in resposta1 and "mewing" not in resposta1:
        print("\n❌ ERROU!")
        print(
            "💥 Mensagem do sistema: Você perdeu aura, você não é mais uma brainrot!"
        )
        return

    print("✅ Resposta certa! Subiu +100 de aura.\n")
    time.sleep(1)

    # Pergunta 2
    resposta2 = (
        input(
            "Pergunta 2: O que você faz quando alguém te olha de ponta a cabeça? "
        )
        .strip()
        .lower()
    )

    if "mewing" not in resposta2 and "Perdeu algo?" not in resposta2:
        print("\n❌ ERROU!")
        print(
            "💥 Mensagem do sistema: Você perdeu aura, você não é mais uma brainrot!"
        )
        return

    print("✅ Resposta certa! Você é uma Sigma definitiva!")
    print("\n🎉 Parabéns! Você manteve sua aura e continua sendo brainrot!")


# Rodar a chamada
ligacao_para_amiga()