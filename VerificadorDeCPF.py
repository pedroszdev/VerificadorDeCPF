cpf='009811700990'
nove_digitos=cpf[:9]
dez_digitos=cpf[:10]
ultimo_dois_digitos=cpf[9:]
contador_regressivo_1=10
contador_regressivo_2=11
resultado_digito_1=0
resultado_digito_2=0
for digito in nove_digitos:
    resultado_digito_1+= int(digito)*contador_regressivo_1
    contador_regressivo_1-=1
digito_1=(resultado_digito_1*10) %11
digito_1= 0 if digito_1 > 9 else digito_1
for digito in dez_digitos:
    resultado_digito_2 += int(digito)*contador_regressivo_2
    contador_regressivo_2-=1
digito_2=(resultado_digito_2*10) %11
digito_2=0 if digito_2 > 9 else digito_2
if digito_1 == int(ultimo_dois_digitos[0]) and digito_2 == int(ultimo_dois_digitos[1]):
    print('Seu CPF está correto')
else:
    print('Seu CPF não está correto')
