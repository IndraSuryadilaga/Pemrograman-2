# x = int(input("Masukkan nilai x: "))
# y = int(input("Masukkan nilai y: "))
# z = int(input("Masukkan nilai z: "))
a=5
b=6
c=7

charvar = ['a', 'b', 'c']
datavar = [a, b, c]

for char, data in zip(charvar, datavar):
    print(f'Variabel {char} bernilai {data}')

print(f'Jumlah dari a dikali  b dibagi c adalah {float(a*b/c):.4f}')