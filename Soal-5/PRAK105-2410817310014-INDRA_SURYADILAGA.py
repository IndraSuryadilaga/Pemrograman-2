a=5
b=6
x=7
y=8

charvar = ['a', 'b', 'x', 'y']
datavar = [a, b, x, y]

for char, data in zip(charvar, datavar):
    print(f'Variabel {char} bernilai {data}')

print(f'Total sisa bagi dari a dibagi b dan x dibagi y adalah {(a%b)+(x%y)}')
