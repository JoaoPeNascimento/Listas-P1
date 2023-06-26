nome = ['shi', 'chi', 'ko', 'ku', 'ya', 'ma']
parar = 1


def comparar(a, b): 
    return a == b


def separar(palavra):     
    vogal = set('aeiou')
    para = 0
    silabaSep = []
    for i in range(len(palavra)):
        if palavra[i] in vogal:
            silabaSep.append(palavra[para:i + 1])
            para = i + 1
    return silabaSep


def ordenar(palavras2):  
    ordem = False
    idca = 0
    idcb = 0
    c = 0
    while c < len(palavras2):
        if c == 0:
          idcb = nome.index(palavras2[c])
        else:
          idca = nome.index(palavras2[c])
          ordem = comparar(idcb, idca - 1)
          idcb = idca 
        c += 1
    return ordem



armazenar = []     
while parar != 0:
    palavra1 = input()
    silabas = separar(palavra1)
    dentro = []       
    for n in silabas:
        if n in nome:
            nHospital = nome.index(n)
            if nHospital not in armazenar:
                armazenar.append(nHospital)
                dentro.append(n)

    if len(dentro) > 1:
        silOrdenado = ordenar(dentro)
        p = ''
        if silOrdenado and p.join(dentro) == palavra1:
            print(f'A palavra {p.join(dentro)} está toda no nome do hospital. Acertou em cheio, Totoro!')
        else:
            q = ', '
            print(
                f'Lembrei! As sílabas: {q.join(dentro)} estão no nome do hospital. Obrigada, Totoro!')
    elif len(dentro) == 1:
        print(f'Lembrei! A sílaba {dentro[0]} está no nome do hospital. Obrigada, Totoro!')
    else:
        print('Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.')

    armazenar.sort()
    if len(armazenar) == 6:
        parar -= 1
        print('Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!')