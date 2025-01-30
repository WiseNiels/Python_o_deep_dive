#  1. Matriz Transposta
# Dada uma matriz representada por uma lista de listas, gere a transposta usando list comprehension.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Saída esperada:
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]


# 2. Números Primos
# Dado um número n, gere uma lista com todos os números primos até n usando list comprehension.

n = 50

# Saída esperada:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


# 3. Frequência de Caracteres
# Dada uma string, gere um dicionário com a frequência de cada caractere usando list comprehension.

texto = "banana"

# Saída esperada:
# {'b': 1, 'a': 3, 'n': 2}



# 4. Quadrados de Números Ímpares
# Dada uma lista de números inteiros, retorne uma lista contendo os quadrados apenas dos números ímpares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Saída esperada:
# [1, 9, 25, 49, 81]


# 5. Palavras com mais de 5 letras
# Dada uma lista de palavras, gere uma nova lista contendo apenas as palavras que possuem mais de 5 letras.

palavras = ["Python", "é", "uma", "linguagem", "poderosa"]

# Saída esperada:
# ['Python', 'linguagem', 'poderosa']



# 6. Números Felizes
# Um número feliz é um número que, quando você soma o quadrado de seus dígitos repetidamente, chega ao número 1. Gere uma lista contendo todos os números felizes de 1 a 100.


# Saída esperada:
# [1, 7, 10, 13, 19, 23, 28, 31, 32, ...]


# 7. Flatten de Lista Aninhada
# Dada uma lista de listas, gere uma lista única com todos os elementos.

lista_aninhada = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Saída esperada:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


#  8. Anagramas
# Dada uma lista de palavras, gere um dicionário onde as chaves são palavras ordenadas alfabeticamente e os valores são listas com seus respectivos anagramas.

palavras = ["roma", "amor", "carro", "roca", "mar", "ram"]

# Saída esperada:
# {'amor': ['roma', 'amor'], 'carro': ['carro'], 'acor': ['roca'], 'amr': ['mar', 'ram']}


# 9. Múltiplos de 3 e 5
# Gere uma lista com todos os números de 1 a 1000 que são múltiplos de 3 ou 5.

# Saída esperada:
# [3, 5, 6, 9, 10, 12, ..., 999]


# 10. Conversão de Temperaturas
# Dada uma lista de temperaturas em Celsius, converta-as para Fahrenheit usando list comprehension.

celsius = [0, 10, 20, 30, 40]

# Fórmula: (°C × 9/5) + 32 = °F
# Saída esperada:
# [32.0, 50.0, 68.0, 86.0, 104.0]



