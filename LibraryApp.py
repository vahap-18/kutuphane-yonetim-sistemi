import re
import logging
from LibraryEdit import LibraryDatabase
import sys
import os
import keyboard

operation_cancelled = False  

# Mevcut dizini al
current_directory = os.path.dirname(os.path.abspath(__file__))

# Log dosyasının tam yolu
log_file_path = os.path.join(current_directory, 'app.log')

# Loglama yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path, encoding='utf-8'),  
        logging.StreamHandler()  
    ]
)

def print_menu():
    print("""\
*************************************

## KÜTÜPHANE SORGU PANELİ ##

İŞLEMLER:
---------

1. Kitap ekle
2. Kitapları göster
3. Yazar adına göre arama yap
4. Kitap adına göre arama yap
5. Yayınevine göre arama yap
6. Kitap adına göre kitap sil
7. Yazar adına göre kitap sil
8. Kitap adını güncelle
9. Gelişmiş kitap arama

Çıkmak için 'q' tuşuna basın. İşlem sırasında iptal etmek için 'esc' tuşuna basın.

*************************************
    """)

# ESC tuşuna basıldığında çağrılacak fonksiyon
def esc_key_handler():
    global operation_cancelled
    operation_cancelled = True
    logging.info("ESC tuşuna basıldı. İşlem iptal ediliyor...")
    print("\nİşlem iptal edildi. Programdan çıkılıyor...")
    sys.exit()  # Programı kapatmak için

# ESC tuşunu dinlemek için keyboard kütüphanesini kullan
keyboard.add_hotkey('esc', esc_key_handler)

# Kullanıcı girdisi için güvenli giriş fonksiyonu
def secure_input(prompt, input_type):
    while True:
        user_input = input(prompt + " (İptal için 'esc' tuşuna basın): ")
        if user_input == 'esc':  # 'esc' kontrolü
            print("İşlem iptal edildi.")
            logging.info(f"Kullanıcı işlem iptal etti: {prompt}")
            return None
        if validate_input(user_input, input_type):  # Girdiyi doğrula
            return user_input.title()  # İlk harf büyük diğerleri küçük olarak döndür
        else:
            print(f"Geçersiz {input_type}. Lütfen tekrar deneyin.")
            logging.warning(f"Geçersiz {input_type} girişi: {user_input}")

# Giriş doğrulama fonksiyonu
def validate_input(input_string, input_type):
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
    elif input_type == "kriter":  # Kriter doğrulaması
        return input_string.strip().lower() in ["kitap", "yazar", "yayınevi"]
    return False

def confirm_action(action):
    while True:
        confirmation = input(f"{action} işlemini onaylıyor musunuz? (Evet/Hayır): ").lower()
        if confirmation == "evet":
            return True
        elif confirmation == "hayır":
            print(f"{action} işlemi iptal edildi.")
            logging.info(f"Kullanıcı {action} işlemini iptal etti.")
            return False
        else:
            print("Geçersiz giriş. Lütfen 'Evet' veya 'Hayır' yazın.")

def search_books(db):
    global operation_cancelled

    # Arama kriteri iste
    search_criteria = secure_input("Arama yapmak için arama türünü girin (kitap/yazar/yayınevi): ", "kriter")
    if operation_cancelled:  # Eğer işlem iptal edildiyse çık
        return

    # Kullanıcının girdiğini temizle ve küçük harfe çevir
    search_criteria = search_criteria.strip().lower()

    # Kriterlere göre kullanıcıdan bilgi al
    if search_criteria == "kitap":
        book_name = secure_input("Aramak istediğiniz kitap adı: ", "book_name")
        if book_name and not operation_cancelled:
            db.get_data_book_name(book_name.strip())

    elif search_criteria == "yazar":
        author_name = secure_input("Aramak istediğiniz yazar adı: ", "author_name")
        if author_name and not operation_cancelled:
            db.get_data_author(author_name.strip())

    elif search_criteria == "yayınevi":
        publishing_house = secure_input("Aramak istediğiniz yayınevi: ", "publishing_house")
        if publishing_house and not operation_cancelled:
            db.get_data_publishing_house(publishing_house.strip())

# Ana program
def main():
    db = LibraryDatabase("Library.db")
    logging.info("Kütüphane Yönetim Sistemi başlatıldı.")

    while True:
        try:
            print("\n--- Kütüphane Yönetim Sistemi ---\n")
            print_menu()
            option = input("\nİşlem numarasını girin: ")

            if option == 'q':
                print("Programdan çıkılıyor.")
                logging.info("Programdan çıkıldı.")
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
                print(f"\nEklenen kitap {name}.")
                logging.info(f"Kitap eklendi: {name} ({author})")

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

            elif option == "9":
                search_books(db)

            else:
                print("Geçersiz işlem numarası")
                logging.warning(f"Geçersiz işlem numarası: {option}")

        except Exception as e:
            logging.error(f"Beklenmeyen hata: {e}")
            print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    main()
