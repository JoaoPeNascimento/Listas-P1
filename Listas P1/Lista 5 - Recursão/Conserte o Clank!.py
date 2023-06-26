def analise(texto, caracter):
    if texto == '':
        return 0
    else:
        if texto[0] == caracter:
            return 1 + analise(texto[1:], caracter)
        else:
            return 0 + analise(texto[1:], caracter)


sentencas = []
n_sentencas = int(input())
for j in range(n_sentencas):
    sentencas.append(input())

for sentenca in sentencas:
    p_abrir = analise(sentenca, '(')
    p_fechar = analise(sentenca, ')')
    if p_abrir == p_fechar:
        print('Essa sentença está com os parênteses balanceados, HOORAY!')
    elif p_abrir > p_fechar:
        print('A quantidade de parênteses \'(\' está maior que a de \')\', vamos descartá-la')
    else:
        print('A quantidade de parênteses \')\' está maior que a de \'(\', vamos descartá-la')