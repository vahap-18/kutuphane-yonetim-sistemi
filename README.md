
# Kütüphane Yönetim Sistemi

Bu proje, kullanıcıların kitapları yönetmesine olanak tanıyan bir Kütüphane Yönetim Sistemi'dir. SQLite veritabanı kullanılarak geliştirilmiştir. Kullanıcılar, kitap ekleyebilir, güncelleyebilir, silebilir ve mevcut kitapları görüntüleyebilir. Sistem, kitap bilgilerini (isim, yazar, yayınevi, sayfa sayısı ve baskı numarası) kaydeder.

## Özellikler

- **Kitap Ekleme**: Kullanıcılar, yeni kitapların bilgilerini (isim, yazar, yayınevi, sayfa sayısı, baskı numarası) ekleyebilir.
- **Kitap Güncelleme**: Mevcut kitapların bilgileri güncellenebilir.
- **Kitap Silme**: Kullanıcılar, belirli bir kitabı veya bir yazarın tüm kitaplarını silebilir.
- **Kitap Görüntüleme**: Tüm kitaplar veya belirli bir yazarın kitapları tablo formatında görüntülenebilir.
- **Baskı Numarası**: Kitapların baskı numaraları kaydedilir ve gerektiğinde güncellenebilir.
- **Giriş Doğrulama**: Kullanıcıdan alınan bilgiler belirli kriterlere göre (karakter sınırlamaları, geçerlilik) doğrulanır.
- **Kullanıcı Onayı**: Silme ve güncelleme işlemleri öncesinde kullanıcı onayı alınır.

## Kullanıcı Arayüzü

Program, metin tabanlı bir kullanıcı arayüzü sunar. Kullanıcı, aşağıdaki seçeneklerden birini seçebilir:

1. **Kitapları Göster**: Veritabanındaki tüm kitapların listesini gösterir.
2. **Kitap Ekle**: Kullanıcıdan kitap bilgilerini alarak yeni bir kitap ekler.
3. **Kitap adına göre arama yap**: Belirli bir kitabı arar.
4. **Yazara göre arama yap**: Belirli bir yazarın kitaplarını listeler.
5. **Yayınevine göre arama yap**: Belirli bir yayınevinin kitaplarını listeler.
6. **Kitap adını güncelle**: Mevcut bir kitabın adını günceller.
7. **Kitap sil**: Belirli bir kitabı veya bir yazarın tüm kitaplarını siler.
8. **Çıkış**: Programdan çıkış yapar.

## Gereksinimler

- Python 3.x
- SQLite3 (Python ile birlikte gelir)
- `re` ve `contextlib` kütüphaneleri (Python ile birlikte gelir)

## Kurulum

1. **Depoyu Klonlayın**:
   ```bash
   https://github.com/vahap-18/kutuphane-yonetim-sistemi.git
   cd kutuphane-yonetim-sistemi
   ```

2. **Gerekli Kütüphaneleri Yükleyin**: Python ile birlikte gelen kütüphaneler dışında ek bir kurulum gerekmez.

## Kullanım

1. Programı çalıştırın:
   ```bash
   python main.py
   ```

2. Kullanıcı arayüzü üzerinden aşağıdaki işlemleri gerçekleştirin:
   - Kitap eklemek için gerekli bilgileri girin (kitap adı, yazar, yayınevi, sayfa sayısı, baskı numarası).
   - Kitapları görüntülemek için uygun seçeneği seçin.
   - Mevcut bir kitabı güncellemek veya silmek için kitabın adını girin ve onay isteğini cevaplayın.

### Örnek Kullanım

#### Kitap Ekleme

- Kullanıcıdan kitap adı, yazar adı, yayınevi, sayfa sayısı ve baskı numarası istenir.
- Kullanıcı, işlemi iptal etmek için 'esc' tuşuna basabilir.

#### Kitap Silme

- Kullanıcıdan silmek istediği kitabın adını girmesi istenir.
- Kullanıcı onayı alındıktan sonra kitap silinir.

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request açın veya issue oluşturun. Tüm katkılar memnuniyetle karşılanacaktır!

