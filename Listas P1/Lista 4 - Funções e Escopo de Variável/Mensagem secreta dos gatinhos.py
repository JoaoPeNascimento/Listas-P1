n =input()
lista_n = n.split(' ')
lista_c = []
erro = False

for i in range(len(lista_n)):
  lista_n[i] = int(lista_n[i])
  
for n in range(len(lista_n)):
  def traducao():
    carac = chr(lista_n[n])
    lista_c.append(carac)
  if lista_n[n] >= 0 and lista_n[n] <= 49:
    if lista_n[n] > 25:
      lista_n[n] -= 26
      lista_n[n] += 97
    elif lista_n[n] < 25:
      lista_n[n] += 97
    traducao()
  elif lista_n[n] >= 50 and lista_n[n] <= 99:
    if lista_n[n] > 75:
      lista_n[n] -=26
      lista_n[n] += 15
    elif lista_n[n] < 75:
      lista_n[n] += 15
    traducao()
  elif lista_n[n] == 100:
    lista_c.append(' ')
  else:
    erro = True

if erro == True:
  print('Infelizmente os números nao dizem nada')
else:
  for x in range(len(lista_c)):
    print(lista_c[x], end= '')
