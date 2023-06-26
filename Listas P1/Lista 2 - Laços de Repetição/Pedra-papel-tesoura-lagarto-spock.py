pontoshel = 0
pontoraj = 0
n = int(input())
while n > 0:
  n = n -1
  shel = input()
  raj = input()
  if shel == 'lagarto' and raj == 'spock' or shel == 'spock' and raj == 'tesoura' or shel == 'tesoura' and raj == 'lagarto':
    pontoshel = pontoshel + 1
  elif raj == 'lagarto' and shel == 'spock' or raj == 'spock' and shel == 'tesoura' or raj == 'tesoura' and shel == 'lagarto':
    pontoraj = pontoraj + 1
if pontoshel > pontoraj:
  print('BAZINGA! EU SOU O SENHOR DA SALA!')
elif pontoraj > pontoshel:
  print('ENGOLE ESSA, SHELDON!')
elif pontoshel == pontoraj:
  print('Oh não, precisamos de outra rodada.')