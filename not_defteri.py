notlar = []

def not_ekle(not_metni):
       notlar.append(not_metni)
       print(f"Not eklendi: {not_metni}")

def notları_listele():
       if not notlar:
              print("Henüz hiç not eklenmedi!")
       else:
              print("Mevcut notlar:")
              for i, not_metni in enumerate(notlar, 1):
                     print(f"{i}. {not_metni}")

def not_sil(not_numarası):
       try:
              silinen_not = notlar.pop(not_numarası - 1)
              print(f"Silindi: {silinen_not}")
       except IndexError:
              print("Hata: Geçersiz not numarası!")
       except ValueError:
              print("Hata: Lütfen bir sayı giriniz!")

def ana_menü():
       while True:
              print("\nNot Defteri Uygulaması")
              print("1. Not Ekle")
              print("2. Notları Listele")
              print("3. Not Sil")
              print("4. Çıkış")

              secim = input("Bir seçenek seçiniz (1-4): ")

              if secim == "1":
                     yeni_not = input("Eklemek istediğiniz notu yazınız: ")
                     not_ekle(yeni_not)
              elif secim == "2":
                     notları_listele()
              elif secim == "3":
                     try:
                            not_numarasi = int(input("Silmek istediğiniz notun numarasını giriniz: "))
                            not_sil(not_numarasi)
                     except ValueError:
                            print("Hata: Lütfen bir sayı giriniz!")
              elif secim == "4":
                     print("Programdan çıkılıyor...")
                     break
              else:
                     print("Geçersiz seçenek! Lütfen 1 ile 4 arsaında bir değer giriniz!")

ana_menü()