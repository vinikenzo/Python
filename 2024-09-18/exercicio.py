import datetime
data = datetime.datetime.now()
ano_atual = data.year
mes_atual = data.month
dia_atual = data.day

print("Qual é o dia do seu aniversário? ")
dia_nascimento = int(input())

print("Qual é o mês do seu nascimento? ")
mes_nascimento = int(input())

print("Qual é o seu ano de nascimento? ")
ano_nascimento = int(input())

idade = ano_atual - ano_nascimento

if mes_atual > mes_nascimento:
    print("Você ja fez aniversário este ano. ")
elif mes_atual == mes_nascimento:
    if dia_atual > dia_nascimento:
        print("você ja fez aniversário este ano")
    elif dia_nascimento == dia_atual:
        print("Feliz aniversário!")
    else: 
        print("Você ainda não fez aniversário este ano.")
else:
    print("Você ainda não fez aniversário este ano.")                

if mes_atual > mes_nascimento:
    print("Você tem ",idade,"anos")
elif mes_atual == mes_nascimento:
    if dia_atual > dia_nascimento:
        print("Você tem ",idade," anos.")
    elif dia_atual == dia_nascimento:
        print("Você fez ",idade," anos hoje!")    
    else:
        print("Você tem ",idade - 1," anos.")
else:
    print("Você tem ",idade - 1," anos.")            

if idade > 130:
    print("Ta só o pó hein? rsrs.")    
