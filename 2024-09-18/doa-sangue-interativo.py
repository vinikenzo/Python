print("Qual sua idade?")
idade = int (input())

if idade >= 18 and idade <= 59: # simplificação
    print("Pode doar sangue.")

elif idade == 16 or idade == 17:
    print("Você tem autorização dos pais? (S/N)")
    resposta = input()
    if resposta == "s" or resposta == "S":
        print("Pode doar sangue.")
    else: 
        print("Não pode doar sangue")    

elif idade >= 60 and idade <= 69:
    print("Você já doou sangue alguma vez? (S/N)")
    resposta = input()
    if resposta == "S" or resposta == "s":
        print("Pode doar sangue.")
    else:
        print("Não pode doar sangue.")    

else:
    print("Não pode doar sangue.")     