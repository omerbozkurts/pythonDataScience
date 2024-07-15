ogrenciler = ['Ali','Veli','Ayse','Talat','Zeynep','Ece']

for x in enumerate(ogrenciler,1):
    if x[0]<4:
        print(f'Muhendislik Fakultesi {x[0]}. ogrenci: {x[1]}')
    else:
        print(f'Tip Fakultesi {x[0]}. ogrenci: {x[1]}')