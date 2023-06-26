temp = 30
fome = True
internet = 0 
acao = input()

while (acao != 'parar'):
  if acao == 'ir para o grad':
    temp = temp - 5
    internet = internet + 300
  elif acao == 'sair para a rua':
    temp = temp + 5
  elif acao == 'comer uma quentinha':
    fome = False
  elif acao == 'conectar no wifi':
    internet = internet + 100
  else:
    print('Entrada inválida')
  acao = input()

if temp < 30:
  print('Agora sim, está aconchegante')
else:
  print('A temperatura aqui não está agradável')
if fome == True:
  print('Meu corpo precisa de comida')
if internet < 100:
  print('Essa conexão está horrível')

if temp <= 25 and internet >= 300 and fome == False:
  print('Finalmente um lugar preciso para mim!')