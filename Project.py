import re
import time
from SQLiteLearnUdemy import LibraryDatabase


def print_menu():
    print("""\
*************************************

## KÜTÜPHANE SORGUSUNA HOŞGELDİNİZ ##

İŞLEMLER:
---------

1. Kitapları göster
2. Kitap ekle
3. Kitap adına göre arama yap
4. Yazara göre arama yap
5. Yayınevine göre arama yap
6. Kitap adına göre kitap sil
7. Yazar adına göre kitap sil
8. Kitap adını güncelle

Çıkmak için 'q' tuşuna basın. İşlem sırasında iptal etmek için 'esc' tuşuna basın.

*************************************\
    """)

import re

# Giriş doğrulama fonksiyonu
def validate_input(input_string, input_type):
    if input_string == 'esc':  # İptal kontrolü
        return True
    if input_type == "book_name":
        return bool(re.match(r'^[A-Za-z0-9çÇğĞıİöÖşŞüÜ\s\-_,\.;:()]{2,100}$', input_string))
    elif input_type == "author_name":
        return bool(re.match(r'^[A-Za-zçÇğĞıİöÖşŞüÜ\s\-\.]{2,50}$', input_string))
    elif input_type == "publishing_house":
        return bool(re.match(r'^[A-Za-z0-9çÇğĞıİöÖşŞüÜ\s\-_&]{2,50}$', input_string))
    elif input_type == "page_number":
        return input_string.isdigit() and 1 <= int(input_string) <= 10000
    elif input_type == "edition":  # Baskı numarası için pozitif tam sayı kontrolü
        return input_string.isdigit() and int(input_string) > 0
    return False

# Kullanıcı girdisi için güvenli giriş fonksiyonu
def secure_input(prompt, input_type):
    while True:
        user_input = input(prompt + " (İptal için 'esc' tuşuna basın): ")
        if user_input == 'esc':  # 'esc' kontrolü
            print("İşlem iptal edildi.")
            return None
        if validate_input(user_input, input_type):  # Girdiyi doğrula
            return user_input.title()  # İlk harf büyük diğerleri küçük olarak döndür
        else:
            print(f"Geçersiz {input_type}. Lütfen tekrar deneyin.")


def confirm_action(action):
    while True:
        confirmation = input(f"{action} işlemini onaylıyor musunuz? (Evet/Hayır): ").lower()
        if confirmation == "evet":
            return True
        elif confirmation == "hayır":
            print(f"{action} işlemi iptal edildi.")
            return False
        else:
            print("Geçersiz giriş. Lütfen 'Evet' veya 'Hayır' yazın.")

# Ana program
def main():
    db = LibraryDatabase("Library.db")

    while True:
        try:
            print("\n--- Kütüphane Yönetim Sistemi ---")
            print("1. Kitap ekle")
            print("2. Tüm kitapları görüntüle")
            print("3. Yazara göre kitapları görüntüle")
            print("4. Kitap adına göre kitapları görüntüle")
            print("5. Yayınevine göre kitapları görüntüle")
            print("6. Kitap sil")
            print("7. Yazara göre kitap sil")
            print("8. Kitap adını güncelle")
            print("Çıkmak için 'q' tuşuna basın")

            option = input("İşlem numarasını girin: ")

            if option == 'q':
                print("Programdan çıkılıyor.")
                break

            if option == "1":
                name = secure_input("Kitap adı: ", "book_name")
                if name is None: continue
                author = secure_input("Yazar adı: ", "author_name")
                if author is None: continue
                publishing_house = secure_input("Yayınevi: ", "publishing_house")
                if publishing_house is None: continue
                page_number = secure_input("Sayfa sayısı: ", "page_number")
                if page_number is None: continue
                edition = secure_input("Baskı numarası: ", "edition")
                if edition is None: continue

                db.insert_data_user(name, author, publishing_house, page_number, edition)

            elif option == "2":
                db.get_data()

            elif option == "3":
                author_name = secure_input("Yazar adı: ", "author_name")
                if author_name is None: continue
                db.get_data_author(author_name)

            elif option == "4":
                book_name = secure_input("Kitap adı: ", "book_name")
                if book_name is None: continue
                db.get_data_book_name(book_name)

            elif option == "5":
                publishing_house_name = secure_input("Yayınevi adı: ", "publishing_house")
                if publishing_house_name is None: continue
                db.get_data_publishing_house(publishing_house_name)

            elif option == "6":
                book_name = secure_input("Kitap adı: ", "book_name")
                if book_name is None: continue
                if confirm_action(f"'{book_name}' kitabını silme"):
                    db.delete_as_book_name(book_name)

            elif option == "7":
                author_name = secure_input("Yazar adı: ", "author_name")
                if author_name is None: continue
                if confirm_action(f"'{author_name}' yazarıyla ilgili tüm kitapları silme"):
                    db.delete_as_author_name(author_name)

            elif option == "8":
                old_name = secure_input("Eski kitap adı: ", "book_name")
                if old_name is None: continue

                new_name = secure_input("Yeni kitap adı: ", "book_name")
                if new_name is None: continue

                if confirm_action(f"'{old_name}' kitabını '{new_name}' olarak güncelleme"):
                    db.update_book_name(old_name, new_name)

            else:
                print("Geçersiz işlem numarası")

        except Exception as e:
            print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    main()
