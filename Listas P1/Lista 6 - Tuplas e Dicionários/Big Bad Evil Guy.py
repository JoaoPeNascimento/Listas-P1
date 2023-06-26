personagem = {'Bobby':['grande espada', 'armadura media'],
          'Diana':['dardo', 'armadura leve'],
          'Eric':['grande espada', 'armadura pesada'],
          'Hank':['espada', 'armadura media'],
          'Presto':['cajado', 'armadura leve'],
          'Sheila':['espada', 'armadura leve'],
          'Uni':['chifre', 'armadura leve']
}
inimigos = {}
inimigo = input()
def calc_armadura(nome_heroi):
  armadura = personagem[nome_heroi][1]
  armaduras = {'armadura pesada': 1,
                'armadura media': 2,
                'armadura leve': 4 
  }
  
  resultado = armaduras[armadura]
  return resultado
  
  
def calc_dano(nome_heroi):
  arma = personagem[nome_heroi][0]
  armas = {'chifre': 2,
            'cajado': 4,
            'espada': 6,
            'grande espada': 8,
            'dardo': 12
  }


  resultado = armas[arma]
  return resultado
if inimigo == 'Vingador':
  vida = 30
  inimigos['Vingador'] = vida
  
elif inimigo == 'Tiamat':
  vida = 20
  inimigos['Tiamat'] = vida
  
elif inimigo == 'Vingador das Sombras':
  vida = 14
  inimigos['Vingador das Sombras'] = vida
  
else:
  vida = 9
  inimigos[inimigo] = vida
  
turnos = int(input())

contador = 0
while contador < turnos:
  atacou = input()
  if atacou == 'Mestre dos Magos':
    print('Muito obrigado amigo, que nos vejamos novamente um dia')
    break
  else:
    vida -= calc_dano(atacou)
    if vida <= 0:
      print(f'{atacou} executou o ultimo golpe em {inimigo}, estamos livres!')
      break
    contador += calc_armadura(atacou)

if contador >= turnos:
  print(f'Oh nao, {inimigo} e muito forte, este e o fim!') 