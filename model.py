class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida  
        self.ataque = ataque
        self.defesa = defesa
        self.poder = 50  

    def actualizar_vida(self, dano):
        self.vida -= dano
        print(f"A vida de {self.nome} agora é {self.vida}.")

    def actualizar_poder(self):
        self.poder *= 2  
        print(f"O poder de {self.nome} agora é {self.poder}.\n")


class Heroi(Personagem):
    def __init__(self, nome, vida, ataque, defesa, poder):
        super().__init__(nome, vida, ataque, defesa)
        self.poder = poder  
    def atacar(self, inimigo):
        print(f"\n{self.nome} ataca {inimigo.nome} com {self.ataque}.")
        inimigo.actualizar_vida(self.poder)
        self.actualizar_poder()

    def defender(self, inimigo):
        print(f"\n{self.nome} defendeu o ataque de {inimigo.nome} usando {self.defesa}!")


class Guerreiro(Heroi):
    def __init__(self):
        super().__init__(nome="Guerreiro", vida=1500, ataque="Espada", defesa="Escudo", poder=50)


class Mago(Heroi):
    def __init__(self):
        super().__init__(nome="Mago", vida=2000, ataque="Magia", defesa="Manto invisível", poder=100)


class Monstro(Personagem):
    def __init__(self, nome, vida, ataque, defesa, poder):
        super().__init__(nome, vida, ataque, defesa)
        self.poder = poder  

    def atacar(self, heroi):
        print(f"\n{self.nome} ataca {heroi.nome} com {self.ataque}.")
        heroi.actualizar_vida(self.poder)
        self.actualizar_poder()


class Ogre(Monstro):
    def __init__(self):
        super().__init__(nome="Ogre", vida=2000, ataque="Pau", defesa="Mergulho na Lama", poder=50)


class Dragao(Monstro):
    def __init__(self):
        super().__init__(nome="Dragão", vida=3000, ataque="Fogo", defesa="Vôo para longe", poder=100)
