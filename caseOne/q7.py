dersKodu = ['CMP1005','PYS1001','HUK1005','SEN2204']
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for x in list(zip(dersKodu,kredi,kontenjan)):
    print(f'kredisi {x[1]} olan {x[0]} kodlu dersin kontenjani {x[2]} kisidir.')