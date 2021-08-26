salario = float(input())

def calculo():
    porcentagem = percentual / 100
    calculo_porcent = 1 + porcentagem
    novo_salario = salario * calculo_porcent
    reajuste =  novo_salario - salario
    print(f'Novo salario: {round(float(novo_salario))}')
    print(f'Reajuste ganho: {round(reajuste)}')
    print(f'Em percentual: {percentual} %')

if salario >= 0 and salario <= 400.00:
    percentual = 15
    calculo()
elif salario >= 400.01 and salario <= 800.00:
    percentual = 12
    calculo()    
elif salario >= 800.01 and salario <= 1200.00:
    percentual = 10
    calculo()
elif salario >= 1200.01 and salario <= 2000.00:
    percentual = 7
    calculo()
elif salario > 2000.00:
    percentual = 4
    calculo()    
        
     
    

