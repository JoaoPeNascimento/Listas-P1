pokedex = {}
continua = True

while continua != False:
    try:
        l = []
        p = input().split(' ')
        l.append(p)
        nome = l[0][1]
        if l[0][0] == 'ADD':
            if nome in pokedex.values():
              print('Pokémon já adicionado na Pokédex')
            else:
              carac = input()
              pokedex.update({'nome' + nome: nome, 'desc' + nome: carac})
              print('Pokémon adicionado com sucesso')
        elif l[0][0] == 'DESC':
            if nome in pokedex.values():
                print(pokedex['desc'+ nome])
            else:
                print('Ainda não há registro desse Pokémon')
    except EOFError:
        break