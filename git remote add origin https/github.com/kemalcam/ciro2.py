def ciro1(miktar,birim):
    global ciro
    ciro=miktar*birim
    return ciro

satis_miktari =int(input("Satış Miktarını Giriniz:"))
birim_satis=int(input("Birim Satış Fiyatı:"))
sonuc=ciro1(satis_miktari,birim_satis)
topcalisan=25
adambasi=sonuc/topcalisan
print(adambasi)

