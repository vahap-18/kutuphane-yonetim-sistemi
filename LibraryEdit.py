from tabulate import tabulate
import sqlite3
import logging
import os
from contextlib import contextmanager


class LibraryDatabase:
    
    def __init__(self, db_name):
        # db_name'in tam yolunu oluştur
        self.db_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), db_name)
        self.create_table()  # Tabloyu oluştur

    @contextmanager
    def get_db_cursor(self):
        conn = sqlite3.connect(self.db_name)  # Bağlantı için db_name kullan
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

    def insert_data_user(self, name, author, publishing_house, page_number, edition):
        with self.get_db_cursor() as cursor:
            cursor.execute(""" 
            INSERT INTO Books (Name, Author, PublishingHouse, PageNumber, Edition)
            VALUES (?, ?, ?, ?, ?)
            """, (name, author, publishing_house, page_number, edition))
            logging.info(f"Inserted book: {name} ({author})")

    def get_data(self):
        with self.get_db_cursor() as cursor:
            cursor.execute("SELECT * FROM Books")
            rows = cursor.fetchall()
            logging.info(f"Retrieved {len(rows)} books")

            if rows:
                headers = ["ID", "Kitap Adı", "Yazar", "Yayınevi", "Sayfa Sayısı", "Baskı Numarası"]
                print(tabulate(rows, headers, tablefmt="grid"))
            else:
                print("Kütüphanede kayıtlı kitap bulunamadı.")

    def get_data_book_name(self, book_name):
        with self.get_db_cursor() as cursor:
            cursor.execute("SELECT * FROM Books WHERE Name = ?", (book_name,))
            rows = cursor.fetchall()
            logging.info(f"Searched by book name: {book_name}, found {len(rows)} results")

            if rows:
                headers = ["ID", "Kitap Adı", "Yazar", "Yayınevi", "Sayfa Sayısı", "Baskı Numarası"]
                print(tabulate(rows, headers, tablefmt="grid"))
            else:
                print(f"{book_name} isimli kitap bulunamadı.")

    def get_data_author(self, author_name):
        with self.get_db_cursor() as cursor:
            cursor.execute("SELECT * FROM Books WHERE Author = ?", (author_name,))
            rows = cursor.fetchall()
            logging.info(f"Searched by author name: {author_name}, found {len(rows)} results")

            if rows:
                headers = ["ID", "Kitap Adı", "Yazar", "Yayınevi", "Sayfa Sayısı", "Baskı Numarası"]
                print(tabulate(rows, headers, tablefmt="grid"))
            else:
                print(f"{author_name} isimli yazarın kitapları bulunamadı.")

    def get_data_publishing_house(self, publishing_house_name):
        with self.get_db_cursor() as cursor:
            cursor.execute("SELECT * FROM Books WHERE PublishingHouse = ?", (publishing_house_name,))
            rows = cursor.fetchall()
            logging.info(f"Searched by publishing house: {publishing_house_name}, found {len(rows)} results")

            if rows:
                headers = ["ID", "Kitap Adı", "Yazar", "Yayınevi", "Sayfa Sayısı", "Baskı Numarası"]
                print(tabulate(rows, headers, tablefmt="grid"))
            else:
                print(f"{publishing_house_name} isimli yayınevine ait kitap bulunamadı.")

    def delete_as_book_name(self, book_name):
        with self.get_db_cursor() as cursor:
            cursor.execute("DELETE FROM Books WHERE Name = ?", (book_name,))
            logging.info(f"Deleted book by name: {book_name}")
            print(f"{book_name} isimli kitap silindi.")

    def delete_as_author_name(self, author_name):
        with self.get_db_cursor() as cursor:
            cursor.execute("DELETE FROM Books WHERE Author = ?", (author_name,))
            logging.info(f"Deleted books by author: {author_name}")
            print(f"{author_name} isimli yazara ait tüm kitaplar silindi.")

    def update_book_name(self, old_name, new_name):
        with self.get_db_cursor() as cursor:
            cursor.execute("UPDATE Books SET Name = ? WHERE Name = ?", (new_name, old_name))
            logging.info(f"Updated book name from {old_name} to {new_name}")
            print(f"{old_name} isimli kitap, {new_name} olarak güncellendi.")
