def endeks():
  while True:
    try:
      boy = float(input("Metre Cinsinden Boyunuzu Giriniz (örnek: 1.85) : "))
      break
    except ValueError:
      print("Hatalı boy değeri girdiniz tekrar deneyin (örnek: 1.85)")
    
  while True:
    try:
      kilo = float(input("Kilonuzu Giriniz (örnek: 56.7) : "))
      break
    except ValueError:
        print("Hatalı kilo değeri girdiniz tekrar deneyin (örnek: 56.7) ")
  return kilo / boy ** 2      
  
  
print(endeks())           
    
