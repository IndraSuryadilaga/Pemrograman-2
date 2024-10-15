a=5
b=6
c=7

charvar = ['a', 'b', 'c']
datavar = [a, b, c]

for char, data in zip(charvar, datavar):
    print(f'Variabel {char} bernilai {data}')

print(f'apakah a sama dengan b? jawabanya adalah {int(a==b)}')
print(f'apakah b lebih besar c? jawabanya adalah {int(a>b)}')
print(f'apakah a tidak sama dengan b? jawabanya adalah {int(a!=b)}')