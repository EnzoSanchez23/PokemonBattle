#Importações de Bibliotecas
import random
import time
import os

#Criação de Variaveis
endGame = False
turno = 0
index = 1

#Dicinarios indivduais para os Pokemons
dicPikachu = {
    "Nome": "Pikachu",
    "Vida": 50,
    "Atq1": "Tackle",
    "Atq2": "Choque do Trovão"
}

dicSquirtle = {
    "Nome": "Squirtle",
    "Vida": 50,
    "Atq1": "Tackle",
    "Atq2": "Bubble"
}

dicCharmander = {
    "Nome": "Charmander",
    "Vida": 50,
    "Atq1": "Tackle",
    "Atq2": "Ember"
}

dicBulbasaur = {
    "Nome": "Bulbasaur",
    "Vida": 50,
    "Atq1": "Tackle",
    "Atq2": "Vine Whip"
}

#Lista de Dicionarios
pokemon = [dicPikachu, 
           dicSquirtle,
           dicCharmander,
           dicBulbasaur]

#Laço de repetição para mostrar na tela a Lista
print("Escolha um Pokemon: ")
for item_lista in pokemon:
    print(f'{index} {item_lista.get("Nome")}')
    index +=1

#Entrada de valor
playerNumber = int(input("Escolha seu Pokemon: "))

#Variaveis com valor da Lista e valor aleatorio
playerPick = pokemon[playerNumber-1]
botPick = pokemon[random.randrange(0, len(pokemon))]


print("\nSeu Pokemon:", playerPick.get("Nome"))
print("\nPokemon do oponente:", botPick.get("Nome"), "\n")
print("-----INICIANDO BATALHA-----")

time.sleep(5)

#Função para limpar console
def LimpaConsole():
    os.system('cls')

#Função com parametro e acesso as Chave-Valor dos dicionarios
def MostrarVida(sidePlaying):
    print(f'Pokemon: {sidePlaying.get("Nome")} - Vida: {sidePlaying.get("Vida")}\n')

def EscolheMostraAtaque(sidePlaying):
    print("Escolha seu ataque: \n")
    print(f'1 - {sidePlaying.get("Atq1")} | 2 - {sidePlaying.get("Atq2")}')
    atkPick = int(input("Digite o numero do ataque: "))
    return atkPick

def TomarDano(p1, p2, atk=None):

    chaves = ["Atq1", "Atq2"]

    danoFraco = random.randint(1,7)
    danoForte = random.randint(8,12)

    randAtk = random.choice(chaves)

    if(turno % 2 == 0):
        print(f'\n{p2.get("Nome")} usou {p2.get(randAtk)}')
        if randAtk == chaves[0]:
            p1["Vida"] -= danoFraco
        else:
            p1["Vida"] -= danoForte
    
    else:
        print(f'\n{p1.get("Nome")} usou {p1.get(f'Atq{atk}')}')
        if atk == 1:
            p2["Vida"] -= danoFraco
        else:
            p2["Vida"] -= danoForte

#Laço de repetição para sempre
while not endGame:
    turno += 1
    LimpaConsole()

    print(f'\n-----Turno {turno}-----')

    print("Você: ")
    MostrarVida(playerPick)
    
    print("Adversario: ")
    MostrarVida(botPick)

    time.sleep(3)

    #Condicionais
    if turno % 2 != 0:
        atkPick = EscolheMostraAtaque(playerPick)
        TomarDano(playerPick, botPick, atkPick)
    else:
        TomarDano(playerPick, botPick)
    
    if(playerPick.get("Vida") <= 0):
        print(f'\n{playerPick.get("Nome")} desmaiou! Você Perdeu.')
        endGame = True

    elif botPick.get("Vida") <= 0:
        print(f'\n{botPick.get("Nome")} desmaiou! Você Venceu.')
        endGame = True

    time.sleep(3)