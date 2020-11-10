#import sqlite3

#con = sqlite3.connect("kütüphane.db")

#cursor = con.cursor()
#
#def tablo_olustur():
#    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa Sayısı INT)")
#    con.commit()

#tablo_olustur()
#con.close()

import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa Sayısı INT)")
    con.commit()
def veri_ekle():
    cursor.execute("Insert into kitaplık Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
# Kullanıcıdan gelen bilgileri eklemek için şu veri ekleme yöntemi kullanılır.

def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
#isim = input("İsim:")
#yazar = input("Yazar:")
#yayınevi = input("Yayınevi:")
#sayfa_sayısı = int(input("Sayfa Sayısı:"))
#veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı)

# Tablodaki Verileri Çekmek İstersek 3 tane sql sorgusu kullanılır.Bunlar;

# Select * From kitaplık : Tablodaki tüm bilgileri almamızı sağlar.
# Select İsim,Yazar From kitaplık : Tablodan sadece isim ve yazar özelliklerini almamızı sağlar.
# Select *  From kitaplık where Yayınevi = 'Everest': Sadece Yayınevi özelliği Everest olanları alır.

def verileri_al():
    cursor.execute("Select * From kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri")
    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri")
    for i in liste:
        print(i)

def verileri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi = ?",(yayınevi,))
    liste = cursor.fetchall()
    print("Kitaplık Tablosunun Yayınevi Bilgileri")
    for i in liste:
          print(i)

# Tablodaki Verileri Güncellemek için;

def verileri_guncelle(eski_yayınevi,yeni_yayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi = ?",(yeni_yayınevi,eski_yayınevi))
    con.commit()


# Tablodaki Verileri Silmek İstersek;

def verileri_sil(yazar):
    cursor.execute("Delete From kitaplık where Yazar = ?",(yazar,))
    con.commit()
verileri_sil("Ahmet Ümit")
verileri_guncelle("Doğan Kitap","Everest")
#Bu durumda tablo içindeki Doğan Kitap Yayınevleri Everest şeklinde güncellendi.
verileri_al()
#verileri_al2()
#verileri_al3("Everest")
con.close()
