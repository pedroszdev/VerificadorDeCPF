cpf=input('Digite seu CPF: ').split('-')
cpf_semponto=cpf[0].split('.')
multi=10
multi_numeros=[]
primeiro_digito_cpf = int(cpf[1][0])
for partecpf in cpf_semponto:
    for numero in partecpf:
        numeroint = int(numero)
        result=multi*numeroint
        multi_numeros.append(result)
        multi-=1
soma=sum(multi_numeros)
multi10=soma*10
resto_div=multi10%11
primeiro_digito_cpf_da_verificação= 0 if resto_div > 9 else resto_div
if primeiro_digito_cpf_da_verificação == primeiro_digito_cpf:
    print('Seu CPF esta correto')
else:
    print('Seu CPF esta incorreto')