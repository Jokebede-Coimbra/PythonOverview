# Se eu quiser uma tupla de um elemento deve colocar uma ','
tupla = tuple('um',)
print(type(tupla))

cores = ('verde', 'amarelo', 'roxo', 'azul')
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('amarelo'))
print(cores.count('Amarelo')) # Retorna 0 porque não está na lista
print(len(cores))