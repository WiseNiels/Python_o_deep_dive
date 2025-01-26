# Criação de um Closure Simples
# 1. Escreva uma função multiplicador que recebe um número e retorna uma função que, quando chamada, multiplica esse número pelo valor passado inicialmente.

# Exemplo de saída:

multiplicar_2 = multiplicador(2)
print(multiplicar_2(5))  # Saída: 10
print(multiplicar_2(10))  # Saída: 20


# 2.Somador com Closure
# Crie uma função somador que recebe um número e retorna uma função que adiciona esse número a um argumento passado para ela.

# Exemplo de saída:

somar_3 = somador(3)
print(somar_3(4))  # Saída: 7
print(somar_3(10))  # Saída: 13


# 2.Encapsulando Estado com Closure
# Escreva uma função contador que inicializa um contador em zero e retorna uma função que incrementa esse contador toda vez que é chamada.

# Exemplo de saída:

cont = contador()
print(cont())  # Saída: 1
print(cont())  # Saída: 2

# 4.Closure com Parâmetro de Valor Padrão
# Crie um closure que tem um valor padrão, e quando chamado, ele somará esse valor ao argumento passado.

# Exemplo de saída:

somar_5 = somador(5)
print(somar_5(7))  # Saída: 12
print(somar_5())  # Saída: 5




# Exercícios sobre Decorators (funcionais e baseados em classe)

# 5.Decorator Simples para Registrar Execução
# Crie um decorator chamado log_execucao que, antes de executar qualquer função, imprime uma mensagem indicando que a função está sendo executada.


# 6.Decorator para Medir Tempo de Execução
# Implemente um decorator tempo_execucao que calcula o tempo que uma função leva para ser executada.



# 7.Decorator com Argumentos
# Crie um decorator chamado verifica_argumento que verifica se o argumento passado para a função é positivo. Caso não seja, levanta uma exceção.


#8. Decorator de Classe para Memoização (Cache)
# 
# Implemente um decorator de classe que armazene os resultados de funções para evitar recomputação. Essa versão deve ser feita usando decorators baseados em classe.

# 9.Decorator de Classe com Argumentos
# Crie um decorator de classe chamado verifica_tipo que verifica se o tipo do argumento da função corresponde ao tipo especificado em um argumento extra do decorator.

