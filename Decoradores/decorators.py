# res = soma(2)
# print(res)


# def n_argumetos(*args, **kwargs):
#     """Funcao que recebe n argumentos"""
#     print(f"args: {args} <====>kwargs: {kwargs}")


# n_argumetos()

# n_argumetos(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, nome="Lucas", idade=25)


from functools import wraps


def decorador(funcao):
    @wraps(funcao)
    def interna(*args, **kwargs):
        """Esta e' a funcao interna"""
        print("antes de decorar")
        print(f"args: {args} <====>kwargs: {kwargs}")
        resultado = funcao(*args, **kwargs)
        print("depois  de decorar")
        return resultado

    return interna


# @decorador
# def soma(a, b):
#     """Esta funcao soma dois numeros"""
#     print("funcao soma")
#     return a + b


# soma(3, 7)


# # soma(3,7)
# print(soma.__qualname__)
# print(soma.__doc__)
# # func_aux = decorador(soma)

# res = func_aux(3, 7)

# soma = decorador(soma)

# print(soma.__qualname__)
# print(soma.__doc__)
# res = soma(3, 7)

# print(func_aux)


# Decorator factory

def multiply_result_by(n):
    def decorator(original_function):
        def new_function(*args, **kwargs):
            result = original_function(*args, **kwargs)
            return result * n

        return new_function

    return decorator


@multiply_result_by(300)
def soma(a, b):
    """Esta funcao soma dois numeros"""
    print("funcao soma")
    return a + b


print(soma(3, 7))   # 20

# decorador = multiply_result_by(2)
# soma = decorador(soma)
# res =soma(3, 7)
# print(res)


# adicao: list = []
# for n in range(4):
#     adicao.append(lambda x: x + n)

# print(adicao[0](10))  # 