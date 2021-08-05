n1 = float(input("Nota 01: "))
n2 = float(input("Nota 01: "))
n3 = float(input("Nota 01: "))
n4 = float(input("Nota 01: "))

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

if media > 7.0:
    print("Média: ", media)
    print("Aluno Aprovado")
    
elif media < 5.0:
    print("Média: ", media)
    print("Aluno Reprovado")
    
elif media >= 5.0 and media <= 6.9:
    print("Média: ", media)
    print("Aluno em Exame")
    
    exame = float(input("Digite a nota do exame:"))
    print("Nota do exame: ", exame)
    soma = (exame + media) / 2
    
    if soma >= 5.0:
        print("Aluno aprovado!!!")
    elif soma <= 4.9:
        print("Aluno reprovado")    
    print("Media final: " , soma) 
    
    
    
    