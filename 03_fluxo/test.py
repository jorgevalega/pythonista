def decorador(func):
    def envoltura(*args, **kwargs):
        print(f"Llamando a {func.__name__} con argumentos {args} {kwargs}")
        return func(*args, **kwargs)
    return envoltura

@decorador
def sumar(a, b):
    return a + b

resultado = sumar(3, 4)
print(f"Resultado: {resultado}")