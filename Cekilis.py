import random

while True:
  try:
    kisi_sayisi = int(input("Çekilişe Kaç Kişi Katılacak: "))
    break
  except ValueError:
    print("Bir sayı girmelisin!")  
    
kisiler = []
for i in range(kisi_sayisi):
  while True:
    try:
      katılacak_kisiler = input("İsim Giriniz: ")
      break
    except ValueError:
      print("Isim'e bir sayı giremezsin!")  
  kisiler.append(katılacak_kisiler)

while True:
  try:
    kazanan_sayısı = int(input("Kaç Kişi Kazansın: "))
    break
  except ValueError:
    print("Bir sayı girmelisiniz!")
      
kazananlar = []
for i in range(kazanan_sayısı):
    while True:
      kazanan = random.choice(kisiler)
      if kazanan not in kazananlar:
        kazananlar.append(kazanan)
        break
print("********** Çekiliş Bilgi **********\n\nÇekilişe Katılanlar: {}\nÇekilişi Kazanacak Sayısı: {}\nÇekilişi Kazananlar: {}".format(kisiler,kazanan_sayısı,kazananlar))    
    
