piada_boa = 0
piada_ruim = 0
piada = str

while (piada != 'Fim do Show!'):
  piada = input()
  if piada != 'Fim do Show!':
    reacao = input()
    if reacao == 'BAZINGA!':
      piada_boa = piada_boa + 1
    else:
      piada_ruim = piada_ruim + 1
  
if piada_boa > (piada_ruim + piada_boa) * 0.6:
  print('BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!')
elif piada_ruim > (piada_boa + piada_ruim) *0.6:
  print('Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!')
else:
  print('Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!')