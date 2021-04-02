pessoal = {'nome':'Adriano','sexo':'M','idade': 28}
print(pessoal)
print(pessoal.keys())
print(pessoal.values())
print(f'\nO {pessoal["nome"]} tem {pessoal["idade"]}\n')

#Para apagar um item, podemos usar del pessoal['sexo']
#Para adicionar um elemento, podemos usar pessoal['peso'] = 80.00


#usando o FOR
for k in pessoal.keys():
    print(k)
for k in pessoal.values():
    print(k)
for k, v in pessoal.items():
    print(f'\n{k} = {v}')