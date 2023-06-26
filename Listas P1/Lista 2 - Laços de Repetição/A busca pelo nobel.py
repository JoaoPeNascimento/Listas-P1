fim = False
progresso = False
feitos = 0

while not fim:
    if not fim:  
      msg = input()
      if msg == 'Começou a Trabalhar na Caltech' and feitos == 0:
        feitos = feitos + 1
        progresso = True
      elif msg == 'Trabalho sobre a String Theory' and feitos == 1:
        feitos = feitos + 1
        progresso = True
      elif msg == 'Ganhar o Chancellor de ciência' and feitos == 2:
        feitos = feitos + 1
        progresso = True
      elif msg == 'Pensar na Teoria de Cooper-Hofstader' and feitos == 3:
        feitos = feitos + 1
        progresso = True
      elif msg == 'Criou a Super Assimetria' and feitos == 4:
        feitos = feitos + 1
        progresso = True 
      elif msg == 'É o fim da Estrada pra Sheldon Cooper' and feitos == 0:
        print('Que potencial desperdiçado...')
        fim = True
      elif msg == 'É o fim da Estrada pra Sheldon Cooper' and feitos == 1:
        print('Tão perto, mas tão longe')
        fim = True
      elif msg == 'É o fim da Estrada pra Sheldon Cooper' and feitos == 2:
        print('Tão perto, mas tão longe')
        fim = True
      elif msg == 'É o fim da Estrada pra Sheldon Cooper' and feitos == 3:
        print('Não desista Sheldon, você ainda têm muito para alcançar!')
        fim = True
      elif msg == 'É o fim da Estrada pra Sheldon Cooper' and feitos == 4:
        print('Não desista Sheldon, você ainda têm muito para alcançar!')
        fim = True
      elif msg == 'É o fim da Estrada pra Sheldon Cooper' and feitos == 5:
        print('Nãoooooo, esse momento ia ser seu Sheldon')
        fim = True
      elif msg == 'Bazinga' and progresso == True:
        feitos -= 1
        progresso = False 
      elif msg == 'Ganhar o Nobel' and feitos == 5:
        fim = True
        print('Você conseguiu Sheldon, o Nobel é seu!!!')
      elif msg == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or msg == 'Leonard seu anão covarde' or msg == 'Tu é muito burro Raj':
        print('Não xingue seus amigos Sheldon!')
        progresso = False
      else:
        progresso = False