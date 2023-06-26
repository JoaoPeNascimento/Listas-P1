n_pedras = int(input())
gohan = {}
picolo = {}

def bubblesort(distancias):
    for passnum in range(len(distancias)-1,0,-1):
        for i in range(passnum):
            if distancias[i]>distancias[i+1]:
                temp = distancias[i]
                distancias[i] = distancias[i+1]
                distancias[i+1] = temp
                

def trans_add(dicionario, x):
  for j in range(n_pedras):
    x[j] = int(x[j])
    for u in range(len(x)):
      dicionario.update({'x'+ str(u): x[u]})

g = input().split(' ')
bubblesort(g)
trans_add(gohan, g)
p = input().split(' ')
bubblesort(p)
trans_add(picolo, p)

confirm = 0
for x in range(n_pedras):
  if gohan['x' + str(x)] == picolo['x' + str(x)]:
    confirm += 1
  else:
    confirm -= 1
if confirm == n_pedras:
  print('Dale Gohan!')
else:
  print('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')