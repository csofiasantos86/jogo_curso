import random
from model import Guerreiro, Mago, Ogre, Dragao
from data import ResultadoRepository, TextoIntroducao


def escolher_heroi():
    print("Escolhe o teu herói:")
    print("1. Guerreiro")
    print("2. Mago")
    escolha = input("Digita o número: ")
    if escolha == '1':
        return Guerreiro()
    elif escolha == '2':
        return Mago()
    else:
        print("Escolha inválida. Tenta novamente.")
        return escolher_heroi()


def escolher_monstro():
    return random.choice([Ogre(), Dragao()])


def batalha(repo_batalha, heroi, monstro):
    defesas_restantes = 5
    atacante = random.choice([heroi, monstro])

    while heroi.vida > 0 and monstro.vida > 0:
        if atacante == heroi:
            heroi.atacar(monstro)
            atacante = monstro
        else:
            print(f"\n{monstro.nome} vai atacar {heroi.nome} com {monstro.ataque}.\n")
            print("Escolhe a tua ação:")
            print(f"1. Defender - Defesas restantes: {defesas_restantes}")
            print("2. Aceitar o ataque")
            acao = input("Digita 1 ou 2: ")

            if acao == '1' and defesas_restantes > 0:
                heroi.defender(monstro)
                defesas_restantes -= 1
                print(f"Defesas restantes: {defesas_restantes}")
            elif acao == '2' or defesas_restantes == 0:
                if defesas_restantes == 0:
                    print(f"Defesas restantes: {defesas_restantes}")
                    print("Não te podes defender mais, não tens mais defesas, vais aceitar o ataque!!!!\n")
                monstro.atacar(heroi)
            else:
                print("Opção inválida. Aceitaste o ataque!\n")
                monstro.atacar(heroi)

            atacante = heroi

    if heroi.vida > 0:
        print(f"\n{heroi.nome} venceu a batalha!")
        repo_batalha.remover_personagem(monstro.nome)
    else:
        print(f"\n{monstro.nome} venceu a batalha!")
        repo_batalha.remover_personagem(heroi.nome)

def main():
    TextoIntroducao.introducao_jogo()
    repo_batalha = ResultadoRepository()

    heroi = escolher_heroi()
    monstro = escolher_monstro()

    repo_batalha.adicionar_personagem(heroi)
    repo_batalha.adicionar_personagem(monstro)

    print(f"\nA batalha entre {heroi.nome} e {monstro.nome} vai começar!\n")
    batalha(repo_batalha, heroi, monstro)


main()
