import random
n=random.randint(3,11)
ilkSayi=(3*n)+1
print("Oyun Kuralları: En fazla 2 veya 1 Düşünüz.")
print("örneğin 25 verilen değerden 2 düşüp 23 yada 1 düşüp 24 yazınız.")
print(ilkSayi)
while ilkSayi >=0:
    try:
        tahmin=int(input("Tahmininizi yapiniz."))
        if ilkSayi-tahmin > 2 or ilkSayi-tahmin < 0 or tahmin==ilkSayi:
            print("Girdiğinz Değer 2 veya 1 den daha fazla , az veya eşittir.Lütfen geçerli bir sayi giriniz...")
        else:
            if tahmin==0:
                print("Kaybettiniz. Üzülmeyin Tekrar Deneyip Yine Kaybedebilirsiniz :)")
                break
            if ilkSayi-tahmin==1:
                ilkSayi=tahmin
                ilkSayi=ilkSayi-2
                print(ilkSayi)
            if ilkSayi-tahmin==2:
                ilkSayi=tahmin
                ilkSayi=ilkSayi-1
                print(ilkSayi)
            if ilkSayi<=0:
                print("Tebrikler Kazandınız Evi Arabayı Üstünüze Yapmaya Hazırım.")
    except:
        print("Lütfen Geçerli Bir Sayi giriniz.")