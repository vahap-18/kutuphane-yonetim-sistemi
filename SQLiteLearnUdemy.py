import sqlite3
import logging
from contextlib import contextmanager

logging.basicConfig(filename='library.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class LibraryDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.create_table()

    @contextmanager
    def get_db_cursor(self):
        conn = sqlite3.connect(self.db_name)
        try:
            cursor = conn.cursor()
            yield cursor
            conn.commit()
        except Exception as e:
            conn.rollback()
            logging.error(f"Database error: {e}")
            raise
        finally:
            conn.close()

    # Tabloya 'Edition' (Baskı Numarası) sütunu ekliyoruz
    def create_table(self):
        with self.get_db_cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Books (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Author TEXT NOT NULL,
                PublishingHouse TEXT NOT NULL,
                PageNumber INTEGER NOT NULL,
                Edition INTEGER NOT NULL
            )
            """)
            logging.info("Books table created or already exists")

    # Kitap eklerken 'Edition' alanını kullanıyoruz
    def insert_data_user(self, name, author, publishing_house, page_number, edition):
        with self.get_db_cursor() as cursor:
            cursor.execute("""
            INSERT INTO Books (Name, Author, PublishingHouse, PageNumber, Edition)
            VALUES (?, ?, ?, ?, ?)
            """, (name, author, publishing_house, page_number, edition))
            logging.info(f"New book added: {name} by {author}, Edition: {edition}")

    def get_data(self):
        with self.get_db_cursor() as cursor:
            cursor.execute("SELECT * FROM Books")
            books = cursor.fetchall()

            if not books:
                print("Hiç kitap bulunmamaktadır.")
                logging.info("No books found.")
                return

            headers = ["ID", "Kitap Adı", "Yazar", "Yayınevi", "Sayfa Numarası", "Baskı Numarası"]
            print(f"{headers[0]:<5} {headers[1]:<20} {headers[2]:<20} {headers[3]:<20} {headers[4]:<15} {headers[5]:<10}")
            print("=" * 90)
            for book in books:
                print(f"{book[0]:<5} {book[1]:<20} {book[2]:<20} {book[3]:<20} {book[4]:<15} {book[5]:<10}")
            logging.info("All books data retrieved")

    def get_data_author(self, author):
        with self.get_db_cursor() as cursor:
            cursor.execute("SELECT * FROM Books WHERE Author = ?", (author,))
            books = cursor.fetchall()
            print(f"Yazarı {author} olan kitap bilgileri:")
            if not books:
                print("Hiç kitap bulunmamaktadır.")
                return
            headers = ["ID", "Kitap Adı", "Yayınevi", "Sayfa Numarası", "Baskı Numarası"]
            print(f"{headers[0]:<5} {headers[1]:<20} {headers[2]:<20} {headers[3]:<15} {headers[4]:<10}")
            print("=" * 70)
            for book in books:
                print(f"{book[0]:<5} {book[1]:<20} {book[3]:<20} {book[4]:<15} {book[5]:<10}")
            logging.info(f"Books by author {author} retrieved")

    def get_data_book_name(self, book_name):
        with self.get_db_cursor() as cursor:
            cursor.execute("SELECT * FROM Books WHERE Name = ?", (book_name,))
            books = cursor.fetchall()
            print(f"Adı {book_name} olan kitap bilgileri:")
            if not books:
                print("Hiç kitap bulunmamaktadır.")
                return
            headers = ["ID", "Yazar", "Yayınevi", "Sayfa Numarası", "Baskı Numarası"]
            print(f"{headers[0]:<5} {headers[1]:<20} {headers[2]:<20} {headers[3]:<15} {headers[4]:<10}")
            print("=" * 70)
            for book in books:
                print(f"{book[0]:<5} {book[2]:<20} {book[3]:<20} {book[4]:<15} {book[5]:<10}")
            logging.info(f"Name is {book_name} books")

    def get_data_publishing_house(self, publishing_house):
        with self.get_db_cursor() as cursor:
            cursor.execute("SELECT * FROM Books WHERE PublishingHouse = ?", (publishing_house,))
            books = cursor.fetchall()
            print(f"Yayınevi {publishing_house} olan kitap bilgileri:")
            if not books:
                print("Hiç kitap bulunmamaktadır.")
                return
            headers = ["ID", "Kitap Adı", "Yazar", "Sayfa Numarası", "Baskı Numarası"]
            print(f"{headers[0]:<5} {headers[1]:<20} {headers[2]:<20} {headers[3]:<15} {headers[4]:<10}")
            print("=" * 70)
            for book in books:
                print(f"{book[0]:<5} {book[1]:<20} {book[2]:<20} {book[4]:<15} {book[5]:<10}")
            logging.info(f"Books by publishing house {publishing_house} retrieved")

    def update_book_name(self, old_name, new_name):
        with self.get_db_cursor() as cursor:
            cursor.execute("""
            UPDATE Books SET Name = ? WHERE Name = ?
            """, (new_name, old_name))
            logging.info(f"Book name updated from {old_name} to {new_name}")

    def delete_as_book_name(self, book_name):
        with self.get_db_cursor() as cursor:
            cursor.execute("DELETE FROM Books WHERE Name = ?", (book_name,))
            logging.info(f"Book deleted: {book_name}")

    def delete_as_author_name(self, author_name):
        with self.get_db_cursor() as cursor:
            cursor.execute("DELETE FROM Books WHERE Author = ?", (author_name,))
            logging.info(f"Books by author {author_name} deleted")