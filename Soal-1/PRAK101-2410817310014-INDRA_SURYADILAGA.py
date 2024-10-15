# x = int(input("Masukkan nilai x: "))
# y = int(input("Masukkan nilai y: "))
# z = int(input("Masukkan nilai z: "))
x=5
y=6
z=7

charvar = ['x', 'y', 'z']
datavar = [x, y, z]

for char, data in zip(charvar, datavar):
    print(f'Variabel {char} bernilai {data}')

print(f'Jumlah variabel tersebut adalah {x+y+z}')
