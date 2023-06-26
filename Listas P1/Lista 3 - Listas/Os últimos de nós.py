#criando lista com mochilas
num_mochilas = int(input())
lista_mochilas = []

#criando lista com nome de pessoas
lista_donos = []
lista_donos.append(input().split(' '))

#adicionando itens fixos
for i in range(num_mochilas):
  fixos = ['Lanterna', 'Omega 3 da top therm']
  lista_mochilas.append(fixos)

#criando lista com tamanhos das mochilas
tam_mochilas = []
for i in range(num_mochilas):
  tamanho = int(input())
  tam_mochilas.append(tamanho)

#adicionando itens
n_itens = int(input())
for i in range (n_itens):
  nome_iten = input()
  local = int(input())
  if tam_mochilas[local] > (len(lista_mochilas[local])):
    lista_mochilas[local].append(nome_iten)
  else:
    print('Mochila cheia. Não vai dar para levar.')

#ações
acao = input()
while acao != 'CHEGAMOS NO CIN!':
    if acao == 'Tirar da mochila':
        tirar_iten = input()
        bolsa_tirar = int(input())
        if tirar_iten in lista_mochilas[bolsa_tirar]:
            lista_mochilas[bolsa_tirar].remove(tirar_iten)
            print(f'{tirar_iten} usado com sucesso da mochila {bolsa_tirar}.')
        else:
            print(f'Você não tem {tirar_iten} na mochila {bolsa_tirar}.')

    elif acao == 'Guardar na mochila':
        colocar_iten = input()
        bolsa_colocar = int(input())
        if len(lista_mochilas[bolsa_colocar]) < tam_mochilas[bolsa_colocar]:
            lista_mochilas[bolsa_colocar].append(colocar_iten)
            print(f'{colocar_iten} adicionado na mochila {bolsa_colocar}.')
        else:
            print(f'Mochila {bolsa_colocar} cheia!')

    else:
        print('Ação inválida.')
    acao = input()

for c in range(num_mochilas):
    print(f'Mochila de {lista_donos[0][c]} chegou assim:')
    for z in range(0, len(lista_mochilas[c])):
        print(lista_mochilas[c][z])
        z += 1
    c += 1