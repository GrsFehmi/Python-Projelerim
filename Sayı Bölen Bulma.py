while True:
  try:
    sayi = int(input("Sayıyı Giriniz: "))
    break
  except ValueError:
    print("Bir sayı girmelisiniz! Lütfen tekrar deneyin.")
  
bolenler = []  
for bolen in range(1,sayi+1):
  if sayi % bolen == 0:
    bolenler.append(bolen)
 
print("********** {} Sayısının Bölenleri **********\n\n{}".format(sayi,bolenler))       
