from datetime import date
ano = int('Digite o ano que você nasceu')
idade = date.today().year - ano
if idade <= 9:
    print('Mirim')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade > 19 and idade <= 20:
    print('Senior')
else:
    print('Master')
