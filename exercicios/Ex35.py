print('-=-' *10)
print('analisador de triângulos')
print('-=-' *10)
a = float(input('Primeiro segmento'))
b = float(input('Segundo segmento'))
c = float(input('Terceiro segmento'))
if a<b+c and b<a+c and c<a+b:
    print('Os segmentos acima podem formar um triangulo')
else:
    print('Os segmentos acima não podem fomrmar um triangulo')
