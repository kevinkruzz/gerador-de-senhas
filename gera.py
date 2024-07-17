import random
def gerar_senha():
    tamanho = 8
    caracteres = 'AaBbCcDdEeFfGgHhIiJjKklLmMnNOoPpQqTtRrSsUuVvWwXxYyZz!@#$%&*_123456789'
    senha = ''
    ...
    for num in range(tamanho):
        aleatorios = random.choice(caracteres)
        senha += aleatorios
    return senha