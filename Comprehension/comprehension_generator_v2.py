# Gerado sob demanda e consome pouca memória.
# Se usar o for não precisa chamar o next, porque ele sabe que se trata do generator
generator = (i ** 2 for i in range(10) if i % 2 == 0)

for numero in generator:
    print(numero)
