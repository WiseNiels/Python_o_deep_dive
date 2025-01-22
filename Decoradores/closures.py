# def minha_funcao(nome, idade=25):
#     print(f"Nome: {nome}, Idade: {idade}")
#     print(f" As variaveis locais sao: {locals()}")


# minha_funcao('Wise')


# def minha_funcao():
#     nome = 'Wise'
#     idade = 25
#     print(f"Nome: {nome}, Idade: {idade}")
#     print(f" As variaveis locais sao: {locals()}")


# minha_funcao()


from datetime import datetime
from time import sleep


# def minha_funcao(agora=datetime.now()):

#     print(f" agoara sao : {agora}")


# def minha_funcao_hora():
#     agora = datetime.now()
#     print(f" agoara sao : {agora}")


# minha_funcao_hora()

# sleep(3)


# minha_funcao_hora()

# a = 10
# def minha_funcao():
#     a = 2000
#     print(a)


# minha_funcao()
# print(a)


# def minha_funcao():
#     global a
#     a = 2000
#     print(a)
#     print(f"local: {locals()}")


# minha_funcao()
# print(a)


# funceos aninhadas


# def funcao_externa():
#     a = 10

#     def funcao_interna():
#         a = 20
#         print(a)

#     funcao_interna()
#     print(a)


# funcao_externa()
# def funcao_externa():
#     a = 10

#     def funcao_interna():
#         nonlocal a
#         a = 20
#         print(a)

#     funcao_interna()
#     print(a)


# funcao_externa()


# funcao_externa()


raca = "humano"

# def funcao_externa():
#     a = 10
#     raca = 'elfo'
#     sobrenome = "Wise"

#     def funcao_interna():
#         global raca
#         nonlocal a
#         nonlocal sobrenome
#         nome = "Wise"
#         idade = 25
#         a = 20
#         print(raca)

#     return funcao_interna
#     # print(a)


# fn = funcao_externa()
# fn()

# print(fn.__code__.co_freevars)
# print(fn.__closure__)


def minha_funcao():
    global raca
    raca = "humano"


def func2():
    print(raca)


func2()
minha_funcao()
# print(globals())

a = 10
a = 12
