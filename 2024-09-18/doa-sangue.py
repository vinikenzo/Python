import datetime
data = datetime.datetime.now()
ano_atual = data.year
# primeiro pergunto o ano de nascimento para calcular a idade
print("Qual o seu ano de nascimento? ")
ano_nascimento = int(input())
idade = ano_atual - ano_nascimento

print("Sua idade é", idade, "anos. ")

#também posso escrever 16 <= idade <= 69
#if idade >= 16 and idade<= 59:
#    print("Pode doar sangue. ")
#elif idade == 16 or idade == 17:
  #  print("Pode doar sangue se tiver autorização dos pais. ")
#elif idade >= 60 and idade <= 69:
 #   print("Pode doar sangue contanto que seja doador já registrado. ")    
#else:
 #   print("Não é possível doar sangue com essa idade. ")        