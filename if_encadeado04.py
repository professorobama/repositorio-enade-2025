print("Exemplo de estrutura condicional encadeada - IF Encadeado")
dias_da_semana = int(input("Digite um número de 1 a 7: "))

def verificar_dia_da_semana(dias_da_semana):
    match dias_da_semana :
        case 1:
            return "Domingo"
        case 2:
            return "Segunda-feira"
        case 3:
            return "Terça-feira"
        case 4:
            return "Quarta-feira"
        case 5:
            return "Quinta-feira"
        case 6:
            return "Sexta-feira"
        case 7:
            return "Sábado"
        case _:    
            return "Não há dia correspondente ao valor digitado!"
print(verificar_dia_da_semana(dias_da_semana))        
        


