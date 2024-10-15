sepA=100000
sepB=200000
dis1=15
dis2=70

charsep = ['A', 'B']    
datasep = [sepA, sepB]
datadis = [dis1, dis2]

for char, data in zip(charsep, datasep):
    print(f'Harga sepatu {char} adalah {data}')

for char, data, dis in zip(charsep, datasep, datadis):
    harga_diskon = int(data - (data * dis/100))
    print(f'Harga sepatu {char} setelah diskon {dis}% adalah {harga_diskon}')
