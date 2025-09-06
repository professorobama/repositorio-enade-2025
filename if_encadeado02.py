print("Exemplo de estrutura condicional encadeada - IF Encadeado")
idade = int(input("Digite a sua idade: "))

if idade < 16:
    print("Você não pode votar!")
elif idade < 18:
    print("Voto opcional!")
else:
    print("Voto obrigatório!")
