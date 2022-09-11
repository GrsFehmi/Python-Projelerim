import random

hesap1 = {
  "name": "Fehmi",
  "lastname": "Gürsoy",
  "hesapno": "980018",
  "girissifre": 2580,
  "bakiye": 10000,
  "cüzdan": 1000,
  "borc": 0,
  "kart" : {
    "kartno":"Kartın Yok",
    "sonkullanım":"Kartın Yok",
    "cvv": "Kartın Yok",
    "sahip": "Kartın Yok"
    }
}

hesap2 = {
  "name": "Ali",
  "lastname": "Veli",
  "hesapno": "48201",
  "girissifre": 9098,
  "bakiye": 5000,
  "cüzdan": 10000,
  "borc": 0,
  "kart" : {
    "kartno":"Kartın Yok",
    "sonkullanım":"Kartın Yok",
    "cvv": "Kartın Yok",
    "sahip": "Kartın Yok"
    }
}
              

def sistem(hesap):
  def kredi(hesap):
    faiz = kredi_miktar * 2.5 / 100
    borc = kredi_miktar + faiz
    hesap["bakiye"] += kredi_miktar
    hesap["borc"] += borc
    print(f"{kredi_miktar} TL Hesabiniza Eklendi. Borcunuz {borc} TL")
    
  def paraGonder(hesap):
    if para_miktar > hesap["bakiye"]:
      print("Bakiyeniz Yetersiz")
    if para_miktar < hesap["bakiye"]:
      gpara = para_miktar + komisyon
      ghesapno = int(input("Para Gönderilecek Kişinin Hesap Numarası: "))       
      hesap["bakiye"] -= gpara
          
  def fatura(hesap):
    #fatura_miktar = random.randint(1,1000)
    if hesap["bakiye"] > fatura_miktar:
      hesap["bakiye"] -= fatura_miktar
      print("Fatura Banka Hesabınizdan Tahsil Edildi.")
    elif hesap["bakiye"] < fatura_miktar:
      if hesap["cüzdan"] > fatura_miktar:
        hesap["cüzdan"] -= fatura_miktar
        print("Fatura Cüzdandan Tahsil Edildi. ")

              
  while True:
    menu = int(input("""********** Grs Bank Mobil **********
    1 - Hesap Bilgileri 
    2 - Bakiye Bilgileri
    3 - Para Çek
    4 - Para Yatır 
    5 - Faturaları Öde 
    6 - Para Gönder(fastPay,havale,eft)
    7 - Kredi Çek(ihtiyaç, taşıt, ev)
    8 - Doviz Kuru
    9 - Kredi Kartı
    10 - En Yakın Şube Nerde
    11 - Kredi Borcu Göster Ve Öde
    
    Seçiminiz: """))
  
    if menu == 1:
      print(f'''
      Isim: {hesap["name"]}
      Soyisim: {hesap["lastname"]}
      Hesap Numarası: {hesap["hesapno"]}
      Giriş Şifresi: {hesap["girissifre"]}
      Bakiye: {hesap["bakiye"]}''')
      
    if menu == 2:
      print(f'Banka Bakiyeniz: {hesap["bakiye"]}\nCüzdan Bakiyeniz: {hesap["cüzdan"]}') # Kredi Borcu Gösterme Eklenecek 
      
    if menu == 3:
      para_cek = int(input("Kaç TL Çekilecek: "))
      if para_cek > hesap["bakiye"]:
        print("Yeterli Bakiyeniz Yok Üzgünüm")
      if para_cek <= hesap["bakiye"]:
        hesap["bakiye"] -= para_cek
        hesap["cüzdan"] += para_cek
        print("Para Cuzdaniniza Eklendi!")  
    if menu == 4:
      para_yatır = int(input("Yatirmak İstediğiniz Para Miktarı: "))
      if para_yatır > hesap["cüzdan"]:
        print("Cüzdanınizda Yeterli Para Yok!")
      if para_yatır <= hesap["cüzdan"]:
        hesap["cüzdan"] -= para_yatır
        hesap["bakiye"] += para_yatır
        print("Banka Hesabiniza Para Yatırıldı")  
      
    if menu == 5:
      faturalar = int(input("""
      Hangi Faturanızı Ödiyeceksiniz
      
      1 - Doğalgaz
      2 - Elektrik
      3 - Su
      4 - İnternet
      5 - Telefon
      
      Seçiminiz: """))
      
      if faturalar == 1:   
        fatura_miktar = random.randint(1,1000)    
        ode = int(input(f"Doğalgaz Borcunuz: {fatura_miktar} TL ödemek için 1 i tuşlayin"))
        if ode == 1:
          fatura(hesap)
        if hesap["bakiye"] < fatura_miktar and hesap["cüzdan"] < fatura_miktar: 
          print("Doğalgaz Faturasını Ödeyemediğin Icin Doğalgaz Kesildi.")  
                                       
      if faturalar == 2:  
        fatura_miktar = random.randint(1,1000)    
        ode = int(input(f"Elektrik Borcunuz: {fatura_miktar} TL ödemek için 1 i tuşlayin"))
        if ode == 1:
          fatura(hesap)
        if hesap["bakiye"] < fatura_miktar and hesap["cüzdan"] < fatura_miktar: 
          print("Elektirik Faturasını Ödeyemediğin Icin Elektrik Kesildi.") 
        
      if faturalar == 3:
        fatura_miktar = random.randint(1,1000)    
        ode = int(input(f"Su Borcunuz: {fatura_miktar} TL ödemek için 1 i tuşlayin"))
        if ode == 1:
          fatura(hesap)
        if hesap["bakiye"] < fatura_miktar and hesap["cüzdan"] < fatura_miktar: 
          print("Su Faturasını Ödeyemediğin Icin Su Kesildi.") 
        
        
      if faturalar == 4:
        fatura_miktar = random.randint(1,1000)    
        ode = int(input(f"Internet Borcunuz: {fatura_miktar} TL ödemek için 1 i tuşlayin"))
        if ode == 1:
          fatura(hesap)
        if hesap["bakiye"] < fatura_miktar and hesap["cüzdan"] < fatura_miktar: 
          print("Internet Faturasını Ödeyemediğin Icin Internet Kesildi.") 
        
        
      if faturalar == 5:
        fatura_miktar = random.randint(1,1000)    
        ode = int(input(f"Telefon Borcunuz: {fatura_miktar} TL ödemek için 1 i tuşlayin"))
        if ode == 1:
          fatura(hesap)
        if hesap["bakiye"] < fatura_miktar and hesap["cüzdan"] < fatura_miktar: 
          print("Telefon Faturasını Ödeyemediğin Icin Telefon Hattınız Kesildi.") 
        
    if menu == 6:
      para_gonder = int(input("""Para Gönderme Seçenekleri:
      1 - Fastpay(%2.5 Komisyon)
      2 - Havale(%1.25 Komisyon)
      3 - Eft(%1 Komisyon)"""))
      
      if para_gonder == 1:
        para_miktar = int(input("Gönderilecek Para Miktarı: "))
        komisyon = para_miktar * 2.5 / 100
        gisim = input("Para Gönderilecek Kişinin Ismi Soyismi: ")
        paraGonder(hesap)
        print(f"{gisim} Adlı Kişiye {para_miktar} TL Gönderildi Ve {komisyon} TL komisyon kesildi..")
        
        
        
      if para_gonder == 2:
        para_miktar = int(input("Gönderilecek Para Miktarı: "))
        komisyon = para_miktar * 1.25 / 100
        gisim = input("Para Gönderilecek Kişinin Ismi Soyismi: ")
        paraGonder(hesap)
        print(f"{gisim} Adlı Kişiye {para_miktar} TL Gönderildi Ve {komisyon} TL komisyon kesildi..")
        
        
      if para_gonder == 3:
        para_miktar = int(input("Gönderilecek Para Miktarı: "))
        komisyon = para_miktar * 1 / 100
        gisim = input("Para Gönderilecek Kişinin Ismi Soyismi: ")
        paraGonder(hesap)
        print(f"{gisim} Adlı Kişiye {para_miktar} TL Gönderildi Ve {komisyon} TL komisyon kesildi..")
        
        
          
    if menu == 7:
      secim = int(input("""
      1 - Taşıt Kredisi
      2 - Konut Kredisi 
      3 - İhtiyaç Kredisi"""))
      
      if secim == 1:
        kredi_miktar = int(input("Taşıt Kredisi Miktarı: "))
        if kredi_miktar  <= 250000:
          kredi(hesap)
        else:
          print("250.000 TL den fazla Taşıt kredi veremeyiz.")  
      if secim == 2:
        kredi_miktar = int(input("Konut Kredisi Miktarı: "))
        if kredi_miktar  <= 10000000:
          kredi(hesap)
        else:
          print("10.000.000 TL den fazla Konut kredi veremeyiz.")  
      if secim == 3:
        kredi_miktar = int(input("Kredi Miktarı: "))
        if kredi_miktar  <= 25000:
          kredi(hesap)
        else:
          print("25.000 TL den fazla ihtiyaç kredi veremeyiz.")  
          
    if menu == 8: 
      dolar = random.randint(1,20)
      euro = random.randint(1,20)
      sterlin = random.randint(1,20)
      gram = random.randint(500,1000)
      ceyrek = random.randint(1000,1700)
      print(f""" 
      ********** Döviz Kuru **********
      Dolar = {dolar}
      Euro = {euro}
      Sterlin = {sterlin}
      Gram Altın = {gram}
      Çeyrek Altın = {ceyrek}
      
      Satın Al Ve Satma İşlemlerimiz Bakımda!""") #yapmaya usendim
        
           
           
    if menu == 9: 
      secim = int(input("""
      ********** Kredi Kartı ********** 
      1 - Abone Ol
      2 - Kartlarımı Göster
      """))
      
      if secim == 1:
        ad_soyad = input("Adınız Soyadınız: ")
        maas = int(input("Maaş Bilgisi: "))
        if maas > 15000:
          num = random.randint(1,1000000000000000000000)
          sonkullanım = random.randint(2023,2030)
          cvv = random.randint(1000,9999)
          print(f"Kart Olusturuldu")
          hesap["kart"]["sahip"] = ad_soyad
          hesap["kart"]["kartno"] = num
          hesap["kart"]["sonkullanım"] = sonkullanım
          hesap["kart"]["cvv"] = cvv
      if secim == 2: 
        print(f""" 
        ********** Kartlarım **********
        Kart Üzerindeki İsim: {hesap["kart"]["sahip"]}
        Kart No: {hesap["kart"]["kartno"]}
        Kart Son Kullanım: {hesap["kart"]["sonkullanım"]} 
        Kart Cvv: {hesap["kart"]["cvv"]} """) 
        
    if menu == 10:
      km = random.randint(1,50)
      print(f"Size En Yakın Grs Bank {km} Km Uzaklıkta")  
      
    if menu == 11:
      secim = int(input("""
      ********** Kredi **********
      1 - Kredi Borcu 
      2 - Kredi Borcu Öde"""))
      
      if secim == 1:
        print(f'Kredi Borcunuz {hesap["bakiye"]} TL')
        
      if secim == 2:
        kac_tl = int(input("Ne kadar Ödeyeceksiniz: ")) 
        if kac_tl <= hesap["bakiye"]:
          if hesap["borc"] > kac_tl:
            hesap["bakiye"] -= kac_tl
            hesap["borc"] -= kac_tl
            print(f"{kac_tl} TL ödendi.")
          elif hesap["borc"] < kac_tl:
            print("Borcundan Fazla Para Odeyemezsin") 
        if kac_tl > hesap["bakiye"]:
          print("Paranız Yok")    
      
   
giris = int(input("Giriş Sifreniz: "))
if giris == hesap1["girissifre"]:
  print("Giriş Yapıldı.")       
  sistem(hesap1)       
if giris == hesap2["girissifre"]:
  print("Giriş Yapıldı.")       
  sistem(hesap2)
else:
  print("Giriş Başarısız.")         
