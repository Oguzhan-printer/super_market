
# 🛒 SUPERMARKET SYSTEM 🧾

Bu proje, Python kullanarak temel bir **süpermarket alışveriş sistemi** oluşturur. Kullanıcılar alışveriş listesi oluşturabilir, mevcut stoklara göre alışverişini güncelleyebilir, toplam fiyatı hesaplayabilir ve stokları otomatik olarak güncelleyebilir. 🧑‍💻📦

---

## 📦 Envanter (Inventory)

Her ürün için:
- **Fiyat (₺)**  
- **Stok Miktarı**  
- **Kategori**  
bilgilerini içeren bir sözlük (`dictionary`) oluşturulmuştur.

```python
inventory = {
    'Milk': [4, 1000, 'dairy'],
    'Apples': [2, 3, 'fruits'],
    'Onions': [1, 50, 'vegetables'],
    'Oranges': [1.5, 1000, 'fruits'],
    'Bread': [3, 100, 'bakery'],
    'Bananas': [5, 300, 'fruits']
}
```

---

## 🧾 Alışveriş Listesi (Shopping List)

Kullanıcının almak istediği ürünleri ve miktarları içeren bir liste tanımlanır:

```python
shopping_list = [
    ('milk', 1),
    ('apples', 4),
    ('onions', 5),
    ('oranges', 5),
    ('bread', 2),
    ('bananas', 10)
]
```

> ⚠️ Ürün adlarının büyük/küçük harf duyarlılığına dikkat et! `Milk` ve `milk` farklıdır.

---

## 🔧 Fonksiyonlar

### ✅ `check_stock(shopping_list, inventory)`
- Stok yetersizse kullanıcıyı bilgilendirir.
- Mevcut stok kadar ürünü listeye ekler.
- GÜNCELLENMİŞ alışveriş listesi döner.

### 💵 `compute_bill(updated_shopping_list, inventory)`
- Ürün fiyatlarını kullanarak toplam alışveriş tutarını hesaplar.

### 📉 `update_stock(updated_shopping_list, inventory)`
- Satın alınan ürün miktarlarını stoktan düşer.
- Güncellenmiş envanteri döner.

---

## 📈 Örnek Çıktı

```
We dont have enough stock of apples you can buy a maximum amount of 3
Your updated shopping list: [('milk', 1), ('apples', 3), ...]
Total price: 41.5 $
The inventory was updated: {...}
```

---

## 🚀 Nasıl Çalıştırılır?

1. Python yüklü olmalı.
2. Kodları bir `.py` dosyasına yapıştır ve terminalden çalıştır:
```bash
python supermarket.py
```

---

## ✨ Geliştirme Fikirleri

- 🧍‍♂️ Kullanıcıdan dinamik olarak giriş almak
- 📊 Kategorilere göre satış raporu oluşturmak
- 🛍️ Sepet takibi ve kupon sistemleri eklemek
- 💾 Stokları dosyaya kaydetmek / yüklemek

---

💡 **Bu küçük proje, temel Python veri yapıları ve kontrol yapılarının güzel bir uygulamasıdır.** Başlangıç seviyesi için harika bir örnek! 🐍
