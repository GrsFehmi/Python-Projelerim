import time 
import os

while True:
  try:
    saat = int(input("Kaç Saat (Girmek istemiyorsaniz 0 yazın): "))
    dakika = int(input("Kaç Dakika (Girmek istemiyorsaniz 0 yazın): "))
    break
  except:
    print("Hatalı Değer Girdiniz Lütfen Tekrar Deneyin")
saniye = int(input("Kaç Saniye:  "))        
while saniye == 0 and saat == 0 and dakika == 0:
  print("Saniye 0 a eşit olamaz.")
  saniye = int(input("Kaç Saniye: "))
  
if saat != 0:
  ssaat = saat * 3600
else:
  ssaat = 0

if dakika != 0:
  ddakika = dakika * 60
else:
  ddakika = 0
  
saat_dakika_saniye = ssaat + ddakika + saniye

while True:
  os.system('clear') #windows kullananlar clear yazan yeri cls yapsın
  print(saat_dakika_saniye)
  saat_dakika_saniye -= 1
  time.sleep(1)
  if saat_dakika_saniye == 0:
    os.system('clear') #windows kullananlar clear yazan yeri cls yapsın 
    print("Süre Doldu")
    break
