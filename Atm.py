paranız = 20000 #bakiyeniz 
banka  = 0

while True:
  secenekler = int(input("1- Para Çek\n2- Para Yatır\n3- Kart Bilgileri\n4- Bakiye Bilgisi\n5- Havale\n6- Kart İade\n\nSeçiminiz: "))
  if secenekler == 1:
    paraÇek = int(input("Çekmek İstediginiz Para Miktarı: "))
    if paraÇek > banka:
      print("Yeterli bakiyeniz yok!")
      print("Bakiye Miktarınız: ", banka)
    if paraÇek < banka:
      banka = banka - paraÇek
      paranız = paranız + paraÇek
      print("Para Çekildi Yeni Bakiyeniz: ", paranız)
      print("Bankanızda Kalan Para: ", banka)
  if secenekler == 2:
     paraYatır = int(input("Yatırmak İstediginiz Para Miktarı: "))
     if paraYatır > paranız:
       print("Yeterli Paranız Yok!")
       print("Para Miktarınız: ", paranız)
     if paraYatır < paranız:
       banka = paraYatır
       paranız = paranız - paraYatır
       print("Paranız Yatırıldı Yeni Banka Bakiyeniz: ", banka) 
       print("Cüzdanda Kalan Para: ", paranız)
  if secenekler == 3:
    print("Kart Sahibinin Adı Soyadı: Fehmi Gürsoy")
    print("Kart Bolgileri: 1234567890122/09.02/365")
    print("İban: TR00 1203 1038 7482 8103 8391 3302 9384 9193 0293 8492 9222 9182")
  if secenekler == 6:
    print("Lütfen Kartınızı Alınız")
    break
  if secenekler == 4:
    print("Cüzdanızdaki Para Miktarı: ", paranız)
    print("Bankadaki Para Miktarı: ", banka)  
  if secenekler == 5:
    isim_soyisim = input("Havale Yapmak İstediginiz Kişinin Adı Soyadı: ")
    iban = int(input("Iban Giriniz: "))
    miktar = int(input("Göndermek Istediğiniz Miktar: "))
    if paranız < miktar:
      print("Yeterli Paranız Yok!")
    if paranız > miktar:
      print("********** Havale **********\n\nHavale Gönderildi\nGonderen Kişi: Fehmi Gürsoy\nGönderilen Kişi: {}\nGonderilen İban No: {}\nGönderilen Miktar: {}".format(isim_soyisim,iban,miktar))       
     
