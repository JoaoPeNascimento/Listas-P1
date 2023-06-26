suspeitos = input()
lista = suspeitos.split(',')
qntd_suspeitos = len(lista)

while qntd_suspeitos != 1:
  msg = input()
  if msg == 'Não encontrei nada no primeiro suspeito':
    lista.pop(0)
    qntd_suspeitos -= 1
  elif msg == 'O último da lista está limpo':
    lista.pop(-1)
    qntd_suspeitos -= 1
  elif msg == 'Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita':
    if len(lista)%2 == 0:
      lista.pop(int(len(lista)/2))
      qntd_suspeitos -= 1
    elif len(lista)%2 != 0:
      lista.pop(int(len(lista)/2))
      qntd_suspeitos -= 1
  elif msg == 'Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:':
    indice = int(input())
    lista.pop(indice)
    qntd_suspeitos -= 1
  elif msg == 'Acho que temos mais uma opção a ser analisada…':
    novo_sus = input()
    lista.append(novo_sus)
    qntd_suspeitos += 1
  else:
    print('Isso não estava no combinado, a lista vai permanecer do mesmo jeito')
    
print('Acho que encontramos o suspeito. O seu nome é {}, vamos salvar o Sam!'.format(lista[0]))