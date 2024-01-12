pessoa = {'nome': 'Prof(a). Paula', 'idade': 30, 'cursos': ['Inglês','Espanhol']}

pessoa['idade'] = 50
pessoa['cursos'].append('Angular')

print(pessoa)

# pessoa.pop('idade')
print(pessoa)

pessoa.update({'idade': 40, 'sexo': 'F'})
print(pessoa)

del pessoa['cursos']
print(pessoa)

pessoa.clear()
print(pessoa)
