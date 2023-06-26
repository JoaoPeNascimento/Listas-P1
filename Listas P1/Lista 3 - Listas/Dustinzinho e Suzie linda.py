tam_matriz = int(input()) 
matriz = []
s_final = ()

for l in range(tam_matriz):
    linha = input() 
    linha = linha.split(' ')
    for i in range(len(linha)):
        linha[i] = int(linha[i])
    matriz.append(linha)

for i in range(0, tam_matriz):
  for j in range(0, tam_matriz - 1):
    if (i == 0 and j == 0):
      soma_linha = 0
      soma_linha = matriz[i][j] + matriz[i][j+1]
      senha_linha = ((matriz[i][j]), (matriz[i][j+1]))
    elif ((matriz[i][j] + matriz[i][j+1]) > soma_linha):
       soma_linha = matriz[i][j] + matriz[i][j+1]
       senha_linha = (matriz[i][j], matriz[i][j+1])

for j in range(0, tam_matriz-1):
  for i in range(0, tam_matriz-1):
    if i == j:
      if(i == 0 and j == 0):
        soma_diagonal = 0
        soma_diagonal = matriz[i][j] + matriz[i+1][j+1]
        senha_diagonal = (matriz[i][j], matriz[i+1][j+1])
      elif ((matriz[i][j] + matriz[i+1][j+1]) > soma_diagonal):
        soma_diagonal = matriz[i][j] + matriz[i+1][j+1]
        senha_diagonal = (matriz[i][j], matriz[i+1][j+1])

for j in range(0, tam_matriz):
  for i in range(0, tam_matriz-1):
    if(i == 0 and j == 0):
      soma_coluna = 0
      soma_coluna = matriz[i][j] + matriz[i+1][j]
      senha_coluna = (matriz[i][j], matriz[i+1][j])
    elif ((matriz[i][j] + matriz[i+1][j]) > soma_coluna):
      soma_coluna = (matriz[i][j] + matriz[i+1][j])
      senha_coluna = (matriz[i][j], matriz[i+1][j])

    
    
s_final = (senha_linha, senha_coluna, senha_diagonal)
print('Falei que era fácil Dustinzinho...' 
'\nPegando todas os números que formam as combinações dos pares de cada sentido temos...'
'\nPassword: {}{}{}{}{}{}'.format(senha_linha[0],senha_linha[1],senha_coluna[0],senha_coluna[1],senha_diagonal[0],senha_diagonal[1])) 