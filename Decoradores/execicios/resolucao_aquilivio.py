
# Criação de um Closure Simples
# 1. Escreva uma função multiplicador que recebe um número e retorna uma função que, quando chamada, multiplica esse número pelo valor passado inicialmente.

'''

def multiplicador(valor):
    def multiplicar(numero):
        return fator * numero
    return multiplicar

# Exemplo de saída:

multiplicar_2 = multiplicador(2)
print(multiplicar_2(5))  # Saída: 10
print(multiplicar_2(10))  # Saída: 20'''


# 2.Somador com Closure
# Crie uma função somador que recebe um número e retorna uma função que adiciona esse número a um argumento passado para ela.

'''
def somador(valor_inicial):
    def somar(numero):
        return valor_inicial + numero
    return somar


# Exemplo de saída:

somar_3 = somador(3)
print(somar_3(4))  # Saída: 7
print(somar_3(10))  # Saída: 13
'''

# 3.Encapsulando Estado com Closure
# Escreva uma função contador que inicializa um contador em zero e retorna uma função que incrementa esse contador toda vez que é chamada.
'''
def contador():
    cont = 0

    def incrementar():
        nonlocal cont
        cont += 1
        return cont
    return incrementar


# Exemplo de saída:

cont = contador()
print(cont())  # Saída: 1
print(cont())  # Saída: 2

'''

# 4.Closure com Parâmetro de Valor Padrão
# Crie um closure que tem um valor padrão, e quando chamado, ele somará esse valor ao argumento passado.

'''
def somador(valor=0):
    def somar(numero=None):
        return valor if numero is None else valor + numero
    return somar

# Exemplo de saída:

somar_5 = somador(5)
print(somar_5(7))  # Saída: 12
print(somar_5())  # Saída: 5
'''



# Exercícios sobre Decorators (funcionais e baseados em classe)

# 5.Decorator Simples para Registrar Execução
# Crie um decorator chamado log_execucao que, antes de executar qualquer função, imprime uma mensagem indicando que a função está sendo executada.
'''
def log_execucao(func):
    def wrapper(*args, **kwargs):
        print(f"Executando função '{func.__name__}'...")
        return func(*args, **kwargs)
    return wrapper

# Exemplo de uso:
@log_execucao
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Mundo"))

'''
# 6.Decorator para Medir Tempo de Execução
# Implemente um decorator tempo_execucao que calcula o tempo que uma função leva para ser executada.
'''
import time

def tempo_execucao(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Função '{func.__name__}' executada em {fim - inicio:.6f} segundos")
        return resultado
    return wrapper

# Exemplo de uso:
@tempo_execucao
def calcular():
    time.sleep(1)  # Simula uma função demorada
    return "Calculado!"

print(calcular())
'''

# 7.Decorator com Argumentos
# Crie um decorator chamado verifica_argumento que verifica se o argumento passado para a função é positivo. Caso não seja, levanta uma exceção.
'''
def verifica_argumento(func):
    def wrapper(argumento):
        if argumento < 0:
            raise ValueError("O argumento deve ser positivo!")
        return func(argumento)
    return wrapper

# Exemplo de uso:
@verifica_argumento
def dobro(numero):
    return numero * 2

print(dobro(5))  # Saída: 10
# print(dobro(-3))  # Levanta ValueError

'''
#8. Decorator de Classe para Memoização (Cache)
# Implemente um decorator de classe que armazene os resultados de funções para evitar recomputação. Essa versão deve ser feita usando decorators baseados em classe.

'''
class Memoizacao:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        resultado = self.func(*args)
        self.cache[args] = resultado
        return resultado

# Exemplo de uso:
@Memoizacao
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Saída: 55
'''

# 9.Decorator de Classe com Argumentos
# Crie um decorator de classe chamado verifica_tipo que verifica se o tipo do argumento da função corresponde ao tipo especificado em um argumento extra do decorator.

class VerificaTipo:
    def __init__(self, tipo):
        self.tipo = tipo

    def __call__(self, func):
        def wrapper(*args):
            if not isinstance(args[0], self.tipo):
                raise TypeError(f"Argumento deve ser do tipo {self.tipo.__name__}")
            return func(*args)
        return wrapper

# Exemplo de uso:
@VerificaTipo(int)
def quadrado(numero):
    return numero ** 2

print(quadrado(4))  # Saída: 16
# print(quadrado("4"))  # Levanta TypeError


# Nota: Alguns dos exercicios acabei usando o recurso da IA para a sua resolucao, 
# claro que nao copiei direito. Sempre procurei entender a logica dos mesmos.