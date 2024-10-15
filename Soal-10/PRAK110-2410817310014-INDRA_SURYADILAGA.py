import math

alas=5
tinggi=12
miring=math.sqrt(alas**2 + tinggi**2)

print(f'''
Diketahui :
Alas   = {alas} cm
Tinggi = {tinggi} cm\n
Jawab :
Sisi A = {alas} cm
Sisi B = {miring:.0f} cm
Sisi C = {tinggi} cm
Keliling = {alas + tinggi + miring:.0f} cm
Luas     = {alas*tinggi/2:.0f} cm^2''')