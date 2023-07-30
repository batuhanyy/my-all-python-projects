import random
import time
import os
from colorama import Fore

def main():
    kasa_bakiyesi = 5000000
    kullanici_bakiyesi = 1000

    # Kuralları ve Nasıl Oynanır'ı ekrana yazdırma
    kurallar = """
    Kurallar:
    1. Yatırmak istediğiniz bahis miktarı 50 TL ve katları olmalıdır.
    2. Kullanılacak çarpan miktarı 1 ile 10 arasında olmalıdır.
    3. Eli kaybetmeniz durumunda yatırılan para ve çarpan miktarı kadar, kumarhaneye borçlanırsınız.
    4. Oyun sonunda kumarhane kasasının bakiyesi 0 TL'ye düşerse, oyuncu kazanır.
    5. Oyuncu bakiyesi 0 TL'ye düşerse, kumarhane kazanır.
    6. İyi şanslar! ve unutmayın, "Her zaman kumarhane kazanır".
    """

    nasil_oynanir = """
    Nasıl Oynanır:
    1. Yatırmak istediğiniz bahis miktarını girin.
    2. Kullanmak istediğiniz çarpan miktarını girin.
    3. Sonuç bekleyin ve kazanç/kayıp durumunu öğrenin.
    4. Oyunun devam etmesi durumunda yeni bir bahis girin.
    """

    print(Fore.YELLOW + kurallar)
    print(Fore.YELLOW + nasil_oynanir)

    kabul = input("Kuralları kabul ediyor musunuz? (y/n): ")
    if kabul != "y":
        print(Fore.YELLOW + "Oyun başlamadan çıkıldı. Kuralları kabul etmeniz gerekmektedir.")
        return

    def kazandir(bahis_miktari, carpan):
        nonlocal kasa_bakiyesi, kullanici_bakiyesi
        kazanc = bahis_miktari * carpan
        kasa_bakiyesi -= kazanc
        kullanici_bakiyesi += kazanc
        return kazanc

    def somur(bahis_miktari, carpan):
        nonlocal kasa_bakiyesi, kullanici_bakiyesi
        kayip = bahis_miktari * carpan
        kasa_bakiyesi += bahis_miktari
        kullanici_bakiyesi -= kayip
        return kayip

    def oyna():
        nonlocal kasa_bakiyesi, kullanici_bakiyesi
        os.system('cls' if os.name == 'nt' else 'clear')

        print(Fore.YELLOW + f"Güncel bakiyeniz: {kullanici_bakiyesi} TL")
        bahis_miktari = int(input("Yatırmak istediğiniz bahis miktarını girin (50 TL ve katları): "))

        if bahis_miktari % 50 != 0 or bahis_miktari <= 0:
            print(Fore.YELLOW + "Geçersiz bahis miktarı. Lütfen 50 TL ve katları olarak girin.")
            time.sleep(3)
            return

        if bahis_miktari > kullanici_bakiyesi:
            print(Fore.YELLOW + "Yeterli bakiyeniz bulunmamaktadır. Daha düşük bir bahis miktarı girin.")
            time.sleep(3)
            return

        carpan = int(input("Kullanmak istediğiniz çarpan miktarını girin (1 ile 10 arasında): "))

        if carpan < 1 or carpan > 10:
            print(Fore.YELLOW + "Geçersiz çarpan miktarı. Lütfen 1 ile 10 arasında bir değer girin.")
            time.sleep(3)
            return

        print(Fore.YELLOW + f"Yatırılan para: {bahis_miktari} TL")
        print(Fore.YELLOW + f"Tahmini kazancınız: {bahis_miktari * carpan} TL")

        for i in range(3, 0, -1):
            os.system('cls' if os.name == 'nt' else 'clear')  # Terminali temizle
            print(Fore.YELLOW + f"Güncel bakiyeniz: {kullanici_bakiyesi} TL")
            print(Fore.YELLOW + f"Yatırılan para: {bahis_miktari} TL")
            print(Fore.YELLOW + f"Tahmini kazancınız: {bahis_miktari * carpan} TL")
            print(Fore.YELLOW + f"Kalan süre: {i} saniye")
            time.sleep(1)

        if random.random() < 0.5:
            kazanc = kazandir(bahis_miktari, carpan)
            print(Fore.GREEN + f"Tebrikler, kazandınız! Kazancınız: {kazanc} TL")
            time.sleep(3)
        else:
            kayip = somur(bahis_miktari, carpan)
            print(Fore.RED + f"Maalesef, kaybettiniz! Kaybınız: {kayip} TL")
            time.sleep(3)

        if kasa_bakiyesi <= 0:
            print(Fore.RED + "Kumarhane Fedaileri Peşinde! Hemen Burdan Kaç")
            time.sleep(3)

    # Oyun döngüsü
    while kasa_bakiyesi > 0 and kullanici_bakiyesi > 0:
        oyna()

    print(Fore.YELLOW + "Hayat Bitti.")

if __name__ == "__main__":
    main()