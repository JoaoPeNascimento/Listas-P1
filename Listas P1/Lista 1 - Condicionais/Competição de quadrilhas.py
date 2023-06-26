nome = input()
p1 = input()
p2 = input()
p3 = input()
p4 = input()
p5 = input()

erro = 0
casar = 0
pontos = float(0)

if p1 == 'Cumprimento':
  pontos = pontos + 100
elif p1 == 'Balancê':
  pontos = pontos + 50
elif p1 == 'Passeio':
  pontos = pontos + 70
elif p1 == 'Túnel':
  pontos = 0
elif p1 == 'Serrote':
  pontos = pontos + 100
elif p1 == 'Casamento':
  casar = casar + 1
elif p1 == 'Despedida':
  pontos = pontos + 0
elif p1 != 'Cumprimento' or p1 != 'Balancê' or p1 != 'Passeio' or p1 != 'Túnel' or p1 != 'Serrote' or p1 != 'Casamento' or p1 != 'Despedida':
  erro = erro + 1

if p2 == 'Cumprimento':
  pontos = pontos + 10
elif p2 == 'Balancê':
  pontos = pontos + 50
elif p2 == 'Passeio':
  pontos = pontos + 70
elif p2 == 'Túnel':
  pontos = pontos - (pontos * 0.10)
elif p2 == 'Serrote':
  pontos = pontos + 100
elif p2 == 'Casamento':
  casar = casar + 1
elif p2 == 'Despedida':
  pontos = pontos + 0
elif p2 != 'Cumprimento' or p2 != 'Balancê' or p2 != 'Passeio' or p2 != 'Túnel' or p2 != 'Serrote' or p2 != 'Casamento' or p2 != 'Despedida':
  erro = erro + 1

if p3 == 'Cumprimento':
  pontos = pontos + 10
elif p3 == 'Balancê':
  pontos = pontos + 50
elif p3 == 'Passeio':
  pontos = pontos + 70
elif p3 == 'Túnel':
  pontos = pontos - (pontos * 0.10)
elif p3 == 'Serrote':
  pontos = pontos + 100
elif p3 == 'Casamento':
  casar = casar + 1
elif p3 == 'Despedida':
  pontos = pontos + 0
elif p3 != 'Cumprimento' or p3 != 'Balancê' or p3 != 'Passeio' or p3 != 'Túnel' or p3 != 'Serrote' or p3 != 'Casamento' or p3 != 'Despedida':
  erro = erro + 1

if p4 == 'Cumprimento':
  pontos = pontos + 10
elif p4 == 'Balancê':
  pontos = pontos + 50
elif p4 == 'Passeio':
  pontos = pontos + 70
elif p4 == 'Túnel':
  pontos = pontos - (pontos * 0.10)
elif p4 == 'Serrote':
  pontos = pontos + 100
elif p4 == 'Casamento':
  casar = casar + 1
elif p4 == 'Despedida':
  pontos = pontos + 0
elif p4 != 'Cumprimento' or p4 != 'Balancê' or p4 != 'Passeio' or p4 != 'Túnel' or p4 != 'Serrote' or p4 != 'Casamento' or p4 != 'Despedida':
  erro = erro + 1

if p5 == 'Cumprimento':
  pontos = pontos + 10
elif p5 == 'Balancê':
  pontos = pontos + 50
elif p5 == 'Passeio':
  pontos = pontos + 70
elif p5 == 'Túnel':
  pontos = pontos - (pontos * 0.10)
elif p5 == 'Serrote':
  pontos = pontos + 100
elif p5 == 'Casamento':
  casar = casar + 1
elif p5 == 'Despedida':
  pontos = pontos + 35
elif p5 != 'Cumprimento' or p5 != 'Balancê' or p5 != 'Passeio' or p5 != 'Túnel' or p5 != 'Serrote' or p5 != 'Casamento' or p5 != 'Despedida':
  erro = erro + 1

if casar >= 1:
  pontos = pontos*2

if erro >= 1:
  print('Poxa, {}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.'.format(nome))
else:
  print('Parabéns, {}! Bela apresentação. A pontuação foi de {:.1f}!'.format(nome, pontos))