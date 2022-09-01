import random

class MP3():
  def __init__(self,sarki,sarki_listesi = []):
    self.sarki_listesi = ["Rolex", "Habibi"]
    self.ses = 100
    self.calanSarki = sarki
    
  def sarkiSec(self):
    sayac = 1
    for sarki in self.sarki_listesi:
      print("{} - {}".format(sayac,sarki))
      sayac += 1
    sarki_sec = int(input("Çalmasını istediğiniz şarkıyı seçiniz (şarkı numarası yazinız): "))
    self.calanSarki = self.sarki_listesi[sarki_sec - 1] 
    
  def sesArttır(self):
    ses_seviyesi_arttır = int(input("Ses seviyesi ne kadar artsın (örnek: 10) : "))
    if self.ses == 100:
      print("Ses zaten maksimum seviyede")
    else:
      self.ses += ses_seviyesi_arttır
      print("Yeni Ses Seviyesi: ",self.ses)
    
  def sesAzalt(self):
    ses_seviyesi_azalt = int(input("Ses seviyesi ne kadar azalsın (örnek: 10) : "))
    if self.ses == 0:
      print("Ses seviyesi zate minimum seviyede")
    else:
      self.ses -= ses_seviyesi_azalt 
      print("Yeni Ses Seviyesi: ",self.ses)
    
  def rastgeleSarki(self):
    print(random.choice(self.sarki_listesi)) 
    
  def sarkiEkle(self):
    sarki_ismi = input("Eklemek İstediğiniz Şarkının İsmini Yazınız: ")
    self.sarki_listesi.append(sarki_ismi) 
    print("Şarkı Listenize Eklendi.")
    print("Güncel Şarkı Listeniz: ", self.sarki_listesi)
    
  def sarkiSil(self):
    sayac = 1
    for sarki in self.sarki_listesi:
      print("{} - {}".format(sayac,sarki))
      sayac += 1
    sarki_sil = int(input("Silmek İstediğiniz Şarkının Numarasını Giriniz: "))
    self.sarki_listesi.pop(sarki_sil - 1)
    print("Şarkı Listenizden Silindi.")
    print("Güncel Şarkı Listeniz: ", self.sarki_listesi)
    
  def kapat(self):
    print("Mp3 kapatıldı")
    
  def sarkiBilgi(self):
    print("Şarkı Listesi: ", self.sarki_listesi)
    print("Şuan Çalan Şarkı: ", self.calanSarki) 
    print("Ses Seviyesi", self.ses) 

mp3 = MP3("Şuan şarkı çalmıyor",100)

while True:
  secim = int(input("1 - Şarkı Seç\n2 - Ses Arttır\n3 - Ses Azalt\n4 - Rastgele Şarkı Seç\n5 - Şarkı Ekle\n6 - Şarkı Sil\n7 - Çalan Şarkı Bilgisi\n8 - Kapat\n\nSeçminizi Yapınız: "))
  if secim == 1:
    mp3.sarkiSec() 
      
  if secim == 2:
    mp3.sesArttır() 
        
  if secim == 3:
    mp3.sesAzalt()
     
  if secim == 4:
    mp3.rastgeleSarki()
      
  if secim == 5:
    mp3.sarkiEkle()  
      
  if secim == 6:
    mp3.sarkiSil()
    
  if secim == 7:
    mp3.sarkiBilgi()  
      
  if secim == 8:
    mp3.kapat()
    break           
