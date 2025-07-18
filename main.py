from os import system
from time import sleep

def operacao(qnts_digitos):
    if qnts_digitos==nove_digitos:
        contador_regressivo=10
    else:
        contador_regressivo=11
    resultado_digito=0
    for numero in qnts_digitos:
        resultado_digito+= int(numero)*contador_regressivo
        contador_regressivo-=1
    
    digito=(resultado_digito*10) %11
    digito=0 if digito > 9 else digito
    return digito

def menu():
    print('='*30)
    print('VALIDADOR DE CPF'.center(30))
    print('='*30)
    print('1- Validar um CPF')
    print('2- Sair')
    print('-'*30)

def cpf_tratado(cpf):
    cpf_novo=''
    for numero in cpf:
        if numero.isdigit():
            cpf_novo+=numero
    return cpf_novo


while True:
    menu() 
    resp=input('Escolha uma opção: ')
    system('cls')
   
    if resp=='1':
        print('-'*30)
        cpf=input('Digite seu CPF:')
        system('cls')

        cpf_novo=cpf_tratado(cpf)
        if len(cpf_novo)> 11:
            print('-'*30)
            print(f'O número que voce digitou {cpf} não está correto')
            print('-'*30)
            continue
    elif resp=='2':
        break
    
    else:
        print('-'*30)
        print('Você digitou a opção errada')
        print('-'*30)
        continue
    
    nove_digitos=cpf_novo[:9]
    dez_digitos=cpf_novo[:10]
    ultimo_dois_digitos=cpf_novo[9:]

    digito_1=operacao(nove_digitos)
    digito_2=operacao(dez_digitos)

    if digito_1 == int(ultimo_dois_digitos[0]) and digito_2 == int(ultimo_dois_digitos[1]):
        print('-'*30)
        print(f'O cpf {cpf} está correto')
        print('-'*30)
        sleep(2.5)

    else:
        print('-'*30)
        print(f'O cpf {cpf} não está correto')
        print('-'*30)
        sleep(2.5)
