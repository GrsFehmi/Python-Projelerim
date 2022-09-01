import random

sayac = 1
while True:
  zar1 = random.randint(1,6)
  zar2 = random.randint(1,6)
  print("Deneme {}: {} {}".format(sayac, zar1,zar2))
  sayac += 1
  if zar1 == 6 and zar2 == 6:
    print("İki zar 6 geldi program durduruldu.")
    break
  else:
    pass
