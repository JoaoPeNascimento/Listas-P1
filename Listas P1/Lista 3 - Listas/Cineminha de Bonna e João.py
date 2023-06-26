nome = input()
qtd_filmes = int(input())

#criando lista de filmes e notas
lista_filmes = []
for i in range(qtd_filmes):
    lista_filmes.append(input().split('-'))

#transformando as notas em float
for j in range(qtd_filmes):
    lista_filmes[j][1] = float(lista_filmes[j][1])

#bubble sort
for x in range(qtd_filmes):
    troca = False
    for y in range(1, qtd_filmes - x):
        if lista_filmes[y][1] > lista_filmes[y-1][1]:
            lista_filmes[y] , lista_filmes[y-1] = lista_filmes[y-1] , lista_filmes[y]
            troca = True
    if not troca:
        break

print('Os filmes sugeridos por {} são:'.format(nome))
for i in range(qtd_filmes):
    print(f'{lista_filmes[i][0]}- {lista_filmes[i][1]}') 