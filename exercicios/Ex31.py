dist = float(input('Qual é a disância(km)'))
curta = 0.5 * dist
longa = 0.45 * dist
print('Voce fará uma viagem de {}km'.format(dist))
if dist <=200:
    print('O valor da pasagem e R${}'.format(curta))
else:
    print('O valor da passagem e R${:.2f}'.format(longa))
