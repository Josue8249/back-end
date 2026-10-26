num = []
for c in range(0,5):
    num.append(int(input('digite um valor para a posição')))
    print(f'Você digitou os valores{num}')
    print(f'O maior valor digitado foi{max(num)} na posição {num.index(max(num))+1}º')
    print(f'O menor valor digitado foi{min(num)} na posição {num.index(min(num))+1}º')
    
