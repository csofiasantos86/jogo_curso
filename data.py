class ResultadoRepository:
    def __init__(self):
        self.batalha = []  

    def adicionar_personagem(self, personagem):
        self.batalha.append(personagem)

    def obter_personagem(self, nome):
        for personagem in self.batalha:
            if personagem.nome == nome:
                return personagem
        return None

    def remover_personagem(self, nome):
        personagem = self.obter_personagem(nome)
        if personagem:
            self.batalha.remove(personagem)



class TextoIntroducao:
    def introducao_jogo():
        introducao = """
        Bem-vindo ao Reino de Fantasia!

        O Reino de Fantasia está ameaçado por forças sombrias, e só os guerreiros mais valentes ou os magos mais poderosos podem restaurar o equilíbrio e salvar o reino da destruição.

        Tu foste escolhido para esta missão. Com a tua espada afiada ou o poder da magia, terás de enfrentar monstros temíveis, como o feroz Ogre e o temível Dragão, em combates que decidirão o futuro de todos.

        Regras do Jogo:

        1. Escolhe o teu herói: Podes escolher entre ser um Guerreiro, que luta com espada e escudo, ou um Mago, que usa poderosas magias para atacar e defender-se.
        
        2. Monstros aleatórios: Após escolheres o teu herói, irás enfrentar um monstro aleatório. Pode ser um Ogre com a sua força bruta, ou um Dragão, que domina o fogo.

        3. Batalha: Durante a batalha, o monstro e o herói atacam alternadamente. Quando for a tua vez de ser atacado, terás duas opções:
           - 1. Defender: Usarás o teu escudo ou magia defensiva para evitar o ataque do monstro. No entanto, podes defender-te apenas 5 vezes ao longo da batalha.
           - 2. Aceitar o ataque: Podes optar por não te defender e enfrentar o golpe diretamente, perdendo parte da tua vida.

        4. A cada ataque, o atacante duplicará o seu poder, com a experiência ganha!

        5. Fim da batalha: A luta termina quando um dos combatentes perder toda a sua vida. Se o teu herói derrotar o monstro, o Reino de Fantasia dá mais um passo em direção à salvação. Se fores derrotado, o reino continuará em perigo.

        Agora, o destino do reino está nas tuas mãos. Escolhe o teu herói e prepara-te para enfrentar os maiores perigos!
        """
        print(introducao)