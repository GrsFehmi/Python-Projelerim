arabalarım = []
class Galeri():
  def __init__(self,marka,model,fiyat,renk):
    self.gelenMarka = marka
    self.gelenModel = model
    self.gelenFiyat = fiyat
    self.gelenRenk = renk
    
  def bilgiler(self):
    print("Marka: ", self.gelenMarka)
    print("Model: ", self.gelenModel)
    print("Fiyat: ", self.gelenFiyat)
    print("Renk :", self.gelenRenk)
    
 
   
araba1 = Galeri("Lamborghini", "Aventador", "3.000.000", "Sarı")
araba2 = Galeri("Ferrari", "458 Spider", "2.500.000", "Kırmızı")
araba3 = Galeri("Toros", "Yok", "Beleş", "Beyaz")
   
while True:
  sec = int(input("Seçiminizi Yapınız\n\n**********\n\n1 - Lamborgihini\n**********\n2 - Ferrari\n**********\n3 - Toros\n\nSeçim: "))
  while sec < 0 or sec > 3:
      sec = int(input("Lütfen 1 - 3 arasında seçiniz\nTekrar Seç: "))

  if sec == 1:
    araba1.bilgiler()  
    satınAl = int(input("Şatın almak için 1\nGeriye dönmek için 2\nSeçiminiz:"))
    if satınAl == 1:
      arabalarım.append("Lamborgihini")
      print("Hayırlı Olsun Lamborgihini Aldınız\nArabalarınız: ", arabalarım)
    if satınAl == 2:
      pass 
  if sec == 2:
    araba2.bilgiler()
    satınAl = int(input("Şatın almak için 1\nGeriye dönmek için 2\nSeçiminiz:"))
    if satınAl == 1:
      arabalarım.append("Ferrari")
      print("Hayırlı Olsun Ferrari Aldınız\nArabalarınız: ", arabalarım)
    if satınAl == 2:
      pass  
  if sec == 3:
    araba3.bilgiler()
    satınAl = int(input("Şatın almak için 1\nGeriye dönmek için 2\nSeçiminiz:"))
    if satınAl == 1:
      arabalarım.append("Toros")
      print("Hayırlı Olsun Toros Aldınız.\nArabalarınız: ", arabalarım)
    if satınAl == 2:
      pass  
    
         
