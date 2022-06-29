import random


list_words = ["flauta", "piano", "violino", "contrabaixo", "saxofone", "viola" ]

word = random.choice(list_words)
print(word)

tamanho = len(word)
print(tamanho)

print('JOGO DA FORCA- VERSÃO INSTRUMENTOS MUSICAIS')
casinhas = '_' * tamanho
print(casinhas)

list_digitadas = []
chances = 6

letra_digitada = input('Digite uma letra:')
print(letra_digitada)

list_digitadas = []
list_digitadas.append(letra_digitada)
print(list_digitadas)