dict = {
    "lanche1":{
        'id': 1,
        'especificacao': 'Cachorro Quente',
        "preco": 4.00
    },

    "lanche2":{
        'id': 2,
        'especificacao': 'X SALADA',
        "preco": 4.50
    },    

    "lanche3":{
        'id': 3,
        'especificacao': 'X BACON',
        "preco": 5.00
    },
    "lanche4":{
        'id': 4,
        'especificacao': 'Torrada Simples',
        "preco": 2.00
    },              

    "lanche5":{
        'id': 5,
        'especificacao': 'Refrigerante',
        "preco": 1.50
    },       
}

codigo = int(input("Digite o código: "))
qtd = int(input("Digite o quantidade: "))

if codigo == dict['lanche1']['id']:
    preco = dict['lanche1']['preco']
    pagar = preco * qtd 
    print(f'Total R$ {pagar}')

elif codigo == dict['lanche2']['id']:
    preco = dict['lanche2']['preco']
    pagar = preco * qtd 
    print(f'Total R$ {pagar}')

elif codigo == dict['lanche3']['id']:
    preco = dict['lanche3']['preco']
    pagar = preco * qtd 
    print(f'Total R$ {pagar}')

elif codigo == dict['lanche4']['id']:
    preco = dict['lanche4']['preco']
    pagar = preco * qtd 
    print(f'Total R$ {pagar}')

elif codigo == dict['lanche5']['id']:
    preco = dict['lanche5']['preco']
    pagar = preco * qtd 
    print(f'Total R$ {pagar}')            
    
        
    