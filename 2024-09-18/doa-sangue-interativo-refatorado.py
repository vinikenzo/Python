
print("Qual sua idade?")
idade = int(input())

pode_doar = False 

if idade >= 18 and idade <= 59:
    pode_doar = True
elif idade == 16 or idade == 17:
    print("Você tem autorização dos pais? (S/N)")
    resposta = input()
    if resposta == "s" or resposta == "S": 
        pode_doar = True
elif idade >= 60 and idade <= 69:
    print("Você ja doou sangue anteriormente? (S/N)")
    resposta = input()
    if resposta == "s" or resposta == "S" : 
        pode_doar = True

if pode_doar == True:
    print("Você pode doar sangue")
else:
    print("Você não pode doar sangue.")       


    """
    Exercício para sexta-feira:
    *Pegar os campos "month" e "day" da data atual
    *Perguntar o dia e mês de nascimento do usuário
    *Descobrir se a pessoa já fez aniversário este ano e printar uma mensagem de acordo.

    """ 