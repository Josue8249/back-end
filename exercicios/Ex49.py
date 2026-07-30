from datetime import date
maior = 0 
menor = 0
for c in range(1,8):
    ano = int (input(f'Em que ano {c}º pessoa nasceu? '))
    idade = date.today(). year - ano 
    if idade >= 18:
        maior += 1
    else:
            menor += 1
print(f'Ao todo tivemos {maior} pssoas maiores de idade')
print(f'E também tivemos {menor} pessoas maiores e idade')
