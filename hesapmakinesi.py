while True:
    try:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        
        print("Yapmak istediğiniz işlemi seçin:")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        secim = int(input("Seçiminizi yapın (1/2/3/4): "))

        if secim == 1:
            print("Sonuç: ", sayi1 + sayi2)
        elif secim == 2:
            print("Sonuç: ", sayi1 - sayi2)
        elif secim == 3:
            print("Sonuç: ", sayi1 * sayi2)
        elif secim == 4:
            if sayi2 != 0:
                print("Sonuç: ", sayi1 / sayi2)
            else:
                print("Hatalı giriş: bölen 0 olamaz!")
        else:
            print("Geçersiz seçim!")

        devam_et = input("Devam etmek istiyor musunuz? (Evet/Hayır): ")
        if devam_et.lower() != "evet":
            break

    except Exception as e:
        print(f"Bir hata oluştu. Hata: {e}\nLütfen tekrar deneyin.")

