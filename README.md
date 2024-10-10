
# Kütüphane Yönetim Sistemi

Kütüphane Yönetim Sistemi, kullanıcıların kitapları kolayca yönetmelerine, aramalarına ve güncellemelerine olanak tanıyan bir komut satırı uygulamasıdır. Bu sistem, SQLite veritabanını kullanarak kitap bilgilerini saklar ve kullanıcı dostu bir arayüz sunar.

## İçindekiler

- [Başlangıç](#başlangıç)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Örnek Kullanım](#örnek-kullanım)
- [Örnek Çıktılar](#örnek-çıktılar)
- [Log Tutma](#log-tutma)
- [Fonksiyonlar](#fonksiyonlar)
- [Geliştiriciler](#geliştiriciler)
- [Lisans](#lisans)

## Başlangıç

Bu proje, Python programlama dili ve SQLite veritabanı kullanılarak geliştirilmiştir. Kullanıcılar, kitap ekleme, silme, güncelleme ve arama gibi işlemleri kolayca gerçekleştirebilir.

### Gereksinimler

- Python 3.x
- `keyboard` kütüphanesi (Kurulum için: `pip install keyboard`)
- `tabulate` kütüphanesi (Kurulum için: `pip install tabulate`)
- `sqlite3` (Python ile birlikte gelir)

## Kurulum

1. Bu projeyi klonlayın veya ZIP dosyasını indirin.

   ```bash
   git clone https://github.com/kvahap-18/kutuphane-yonetim-sistemi.git
   cd KutuphaneYonetimSistemi
   ```

2. Gerekli kütüphaneleri yükleyin:

   ```bash
   pip install keyboard tabulate
   ```

3. `LibraryApp.py` dosyasını çalıştırın:

   ```bash
   python LibraryApp.py
   ```

## Kullanım

Uygulama çalıştığında, kullanıcılar aşağıdaki işlemleri gerçekleştirebilir:

1. **Kitap Ekleme**: Yeni bir kitap ekleyin.
2. **Kitapları Gösterme**: Kütüphanede kayıtlı olan tüm kitapları görüntüleyin.
3. **Yazar Adına Göre Arama**: Belirli bir yazarın kitaplarını arayın.
4. **Kitap Adına Göre Arama**: Belirli bir kitabı arayın.
5. **Yayınevine Göre Arama**: Belirli bir yayınevine ait kitapları arayın.
6. **Kitap Silme**: Kitap veya yazar adına göre kitapları silin.
7. **Kitap Adını Güncelleme**: Mevcut bir kitabın adını güncelleyin.
8. **Gelişmiş Kitap Arama**: Kullanıcıdan alınan kriterlere göre kitap arama işlemi yapın.

**Çıkmak için** `q` tuşuna basabilir, **işlem sırasında iptal etmek için** `esc` tuşuna basabilirsiniz.

## Örnek Kullanım

### 1. Kitap Ekleme
Uygulama çalıştığında aşağıdaki gibi bir menü görüntülenecektir:

```
--- Kütüphane Yönetim Sistemi ---

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
```

Bu menüden `1` seçeneğini seçtiğinizde, kitap adı, yazar adı, yayınevi, sayfa sayısı ve baskı numarasını girmeniz istenecek.

### 2. Kitapları Gösterme
`2` seçeneğini seçerek kütüphanede kayıtlı olan tüm kitapları görüntüleyebilirsiniz. 

### 3. Kitap Silme
`6` veya `7` numarasını seçerek kitap veya yazar adına göre silme işlemi gerçekleştirebilirsiniz.

## Örnek Çıktılar

### Kitap Ekleme
Kullanıcı bir kitap eklemek istediğinde, aşağıdaki gibi bir girdi istenir:
```
Kitap adı: Yüzüklerin Efendisi
Yazar adı: J.R.R. Tolkien
Yayınevi: İş Bankası Yayınları
Sayfa sayısı: 500
Baskı numarası: 1
```
Başarılı bir ekleme işleminden sonra aşağıdaki gibi bir çıktı alınır:
```
Eklenen kitap Yüzüklerin Efendisi.
```

### Kitapları Gösterme
Kütüphanede birkaç kitap varsa, bu işlemi gerçekleştirdikten sonra aşağıdaki gibi bir çıktı alınır:
```
+----+-------------------------+------------------+--------------------------+-------------+-------------+
| ID | Kitap Adı              | Yazar            | Yayınevi                | Sayfa Sayısı| Baskı Numarası|
+----+-------------------------+------------------+--------------------------+-------------+-------------+
| 1  | Yüzüklerin Efendisi     | J.R.R. Tolkien   | İş Bankası Yayınları     | 500         | 1           |
| 2  | Hayvan Çiftliği        | George Orwell     | Can Yayınları            | 250         | 1           |
+----+-------------------------+------------------+--------------------------+-------------+-------------+
```

### Yazar Adına Göre Arama
Kullanıcı bir yazar adı ile arama yaptığında, aşağıdaki gibi bir çıktı alır:
```
Aramak istediğiniz yazar adı: J.R.R. Tolkien
+----+-------------------------+------------------+--------------------------+-------------+-------------+
| ID | Kitap Adı              | Yazar            | Yayınevi                | Sayfa Sayısı| Baskı Numarası|
+----+-------------------------+------------------+--------------------------+-------------+-------------+
| 1  | Yüzüklerin Efendisi     | J.R.R. Tolkien   | İş Bankası Yayınları     | 500         | 1           |
+----+-------------------------+------------------+--------------------------+-------------+-------------+
```

## Log Tutma

Uygulama, gerçekleştirilen tüm işlemleri kaydetmek için bir log tutma özelliğine sahiptir. Loglar, sistemin performansını izlemek, hata ayıklamak ve kullanıcı etkinliklerini takip etmek için önemlidir. 

### Log Kaydı
Log kayıtları, uygulama dizininde bulunan `app.log` dosyasında saklanır. Aşağıdaki bilgileri içerir:

- **Tarih ve Saat**: İşlemin ne zaman gerçekleştirildiği.
- **İşlem Türü**: Ekleme, silme, güncelleme gibi yapılan işlemlerin türü.
- **Detaylar**: Gerçekleştirilen işlemle ilgili bilgiler (örneğin, eklenen kitabın adı, yazar adı vb.).

### Log Örneği
```
2024-10-10 10:15:23 - INFO - Kitap Eklendi: Yüzüklerin Efendisi, Yazar: J.R.R. Tolkien
2024-10-10 10:20:45 - INFO - Kitap Silindi: Hayvan Çiftliği, Yazar: George Orwell
```

Log tutma özelliği, geliştiricilere sistemdeki etkinlikleri inceleme ve gerektiğinde hataları düzeltme konusunda yardımcı olur.

## Fonksiyonlar

- **secure_input**: Kullanıcı girdilerini güvenli bir şekilde almak için kullanılır.
- **validate_input**: Kullanıcı girdilerini doğrulamak için çeşitli kontroller gerçekleştirir.
- **search_books**: Kullanıcıdan alınan kriterlere göre kitap arama işlemi yapar.
- **confirm_action**: Kullanıcıdan bir işlemi onaylamasını ister.
- **LibraryDatabase**: Veritabanı işlemlerini yönetmek için kullanılan sınıf.
- **log_action**: Yapılan işlemleri kaydetmek için kullanılır. Bu fonksiyon, her işlem sonrası log dosyasına kayıt yapar.

## Geliştiriciler

- [Adınız](https://github.com/vahap-18)
