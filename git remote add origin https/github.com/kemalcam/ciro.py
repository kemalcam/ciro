def adambasi(miktar,birim):
    global adam
    topcalisan=25
    adam=((miktar*birim)/topcalisan)
    return adam

satis_miktari =int(input("Satış Miktarını Giriniz:"))
birim_satis=int(input("Birim Satış Fiyatı:"))
sonuc=adambasi(satis_miktari,birim_satis)
print(sonuc)

