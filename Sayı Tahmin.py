import random
randsayi = random.randint(1,100)
while True:
  tahminsayi = int(input("Bir sayı Giriniz: "))
  if randsayi == tahminsayi:
    print("Doğru")
    break
  elif tahminsayi > randsayi:
    print("Daha Küçük")
  elif tahminsayi < randsayi:
    print("Daha Büyük")
