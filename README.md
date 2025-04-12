# PacMart: Self Service Cashier

Self-Service Cashier adalah program kasir sederhana berbasis Python yang memungkinkan pelanggan mencatat, mengubah, dan menghitung transaksi belanja mereka secara mandiri. 
Program ini cocok untuk simulasi sistem kasir mandiri (self-checkout) dengan fitur yang interaktif dan dinamis dengan menerapkan algoritma struktur data dan paradigma pemrograman objek atau OOP.

## Problem Background

Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia ingin melakukan perbaikan proses bisnis, dengan cara membuat sistem kasir self-service
sehingga customer bisa langsung melakukan aktivitas transaksi, mencakup memasukkan nama, jumlah, dan harga item yang dibeli serta fitur-fitur lainnya.
Setelah melakukan riset, terdapat permasalahan bahwa dibutuhkan seorang Programmer yang mampu mengimplementasikan pembuatan sistem tersebut.

## Objectives

Menyediakan sistem kasir mandiri yang modular dan interaktif untuk manajemen transaksi belanja supermarket, meliputi:

1. Pencatatan penambahan item
2. Pengubahan informasi item
3. Penghapusan informasi item
4. Perhitungan total harga transaksi

## How to Execute the Program?

1. Pastikan Python telah terinstal di perangkat kamu (disarankan Python 3.++).
2. Pastikan semua dependensi telah diinstal, termasuk tabulate. Jika belum, jalankan perintah berikut di terminal:

```python
pip install tabulate
```
3. Buka terminal atau command prompt, lalu navigasikan ke direktori folder tempat file main.py dan script.py disimpan.
4. Jalankan program dengan mengetik _command_ di bawah ini pada terminal:

```python
python main.py
```
5. Ikuti instruksi di layar untuk mulai menggunakan sistem kasir self-service.

## Code Flow Explanation

1. File main.py berfungsi sebagai entry point dari program. Di dalamnya terdapat fungsi main() yang menjalankan _interface_ berbasis terminal (menu) untuk pengguna. Melalui menu ini, pengguna dapat memilih berbagai aktivitas manajemen transaksi seperti menambah, mengubah, menghapus, mengecek, dan menghitung transaksi.

2. Fungsi main() akan terus berjalan dalam loop hingga pengguna memilih keluar dari program. Setiap pilihan yang dipilih pengguna akan memanggil metode yang sesuai dari objek Transaction yang telah dibuat.

3. File script.py berisi program dengan class Transaction, yang menjadi modul untuk dijalankan pada main.py sebagai program utama.

4. Di dalam class Transaction, terdapat berbagai metode sebagai alat bantu dalam fungsionalitas transaksi, seperti:

  - add_item() => memiliki fungsi untuk menambahkan item baru ke transaksi
  ```python
  def add_item(self):
    """Menambahkan item ke dalam daftar transaksi."""
    self.item_name = input('Nama item: ')
    self.item_qty = input('Jumlah: ')
    self.item_price = input('Harga: ')
    self.items[self.item_name.strip().title()] = [int(self.item_qty), int(self.item_price)]
  ```
  
  - update_item_name(), update_item_qty(), update_item_price() => mengubah detail informasi item, meliputi nama, jumlah, dan harga item.
  ```python
  def update_item_name(self):
    """Mengubah informasi nama item pada daftar transaksi."""
    updated_name_items = dict()
    name_target = input('Masukkan nama item yang ingin diubah namanya: ')

    for key, value in self.items.items():
      if name_target.title() == key:
        new_name = input('Masukkan nama item yang baru: ')
        updated_name_items[new_name.title()] = value # Mengganti nama key dengan nama yang baru
        print('Nama item berhasil diubah!')
      else:
        print('Nama item tidak ditemukan!')
        updated_name_items[key] = value

    self.items = updated_name_items

  def update_item_qty(self):
    """Mengubah jumlah item pada daftar transaksi."""
    name_target = input('Item yang ingin diubah: ')
    new_qty = int(input('Jumlah baru: '))
    self.items[name_target][0] = new_qty

  def update_item_price(self):
    """Mengubah nominal harga item pada daftar transaksi."""
    name_target = input('Item yang ingin diubah: ')
    new_price = int(input('Harga baru: '))
    self.items[name_target][1] = new_price
  ```
  - delete_item() => menghapus item tertentu berdasarkan nama item yang di-_input_ oleh pengguna
  ```python
  def delete_item(self):
    """Menghapus item tertentu dari daftar transaksi berdasarkan nama item."""
    item_to_delete = input('Masukkan nama item yang ingin dihapus dari daftar transaksi: ').strip()
    if item_to_delete in self.items:
      self.items.pop(item_to_delete) # Menghapus item tertentu dari dictionary
    else:
      print('Item tidak ditemukan dalam daftar transaksi!')
  ```

  - reset_transaction() => menghapus seuruh item pada self.items
  ```python
  def reset_transaction(self):
    self.items.clear()
  ```
  - check_order() => menampilkan transaksi dalam bentuk tabel menggunakan modul tabulate

  ```python
  def check_order(self):
    """Menampilkan daftar transaksi serta total harga dalam bentuk tabulasi"""

    order_list = [(key, value[0], value[1], value[0] * value[1]) for key, value in self.items.items()]
    if len(self.items) > 0 and '' not in self.items: 
      headers = ['Nama Item', 'Jumlah Item', 'Harga/Item', 'Total Harga']
      print(f'\nFormat item anda sudah benar! Berikut rincian transaksi anda: \n{tabulate(order_list, headers=headers)}')
    elif len(self.items) == 0:
      print('\nTidak ada item yang dapat ditemukan pada daftar transaksi, silakan tambahkan item terlebih dahulu!')
    else:
      headers = ['Nama Item', 'Jumlah Item', 'Harga/Item', 'Total Harga']
      print('\nTerdapat kesalahan input data item!\n')
      print(tabulate(order_list, headers=headers)) 
      print('\nMohon perbaiki kembali format item tidak boleh ada yang kosong! Silakan lengkapi format item terlebih dahulu.')
  ```

  - total_price() => menghitung total harga dengan mengimplementasikan skenario diskon berdasarkan nominal belanja pengguna
  ```python
  def total_price(self):
    """Menampilkan total harga transaksi serta potongannya apabila memenuhi syarat diskon berdasarkan total harga."""
    total_transaction = 0

    for key, value in self.items.items():
      total_transaction += value[0] * value[1] # Menghitung total harga berdasarkan jumlah item * harga/item

if '' in self.items:
      order_list = [(key, value[0], value[1], value[0] * value[1]) for key, value in self.items.items()]
      headers = ['Nama Item', 'Jumlah Item', 'Harga/Item', 'Total Harga']
      ...

    elif total_transaction <= 200000:
      ...

    elif 200000 < total_transaction <= 300000:
      disc = 0.05
      ...

    elif 300000 < total_transaction <= 500000:
      disc = 0.08
      ...

    elif total_transaction > 500000:
      disc = 0.10
      ...
  ```

## Test Case Result

### Test 1 

Customer menambahkan dua item baru menggunakan method add_item() dengan item yang ditambahkan sebagai berikut:
- Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
- Nama Item: Pasta Gigi, Qty: 3, Harga: 15000

**Expected Output:**

![image](https://github.com/user-attachments/assets/48bbf7de-883b-4013-9e0c-2c8c2043d473)

**Actual Output:**

![image](https://github.com/user-attachments/assets/33824371-5940-499c-ad82-a1d56e189e55)

### Test 2

Customer salah membeli salah satu item dari belanja yang sudah ditambahkan sebelumnya melalui method add_item(), kemudian Customer
ingin menghapus item dengan menggunakan method delete_item(). Item yang dihapus adalah Pasta Gigi.

**Expected Output:**

![image](https://github.com/user-attachments/assets/99e32dd0-37c3-4409-9d46-e644a5afcb43)

**Actual Output:**

![image](https://github.com/user-attachments/assets/75e6e72b-bf83-463d-bf6c-3190f7e8eea1)

### Test 3

Setelah diperiksa kembali, customer salah memasukkan semua item yang ingin dibelanjakan. Alih-alih menghapus satu-satu, customer
cukup menggunakan method reset_transaction() untuk menghapus semua item yang telah ditambahkan sebelumnya.

**Expected Output:**

![image](https://github.com/user-attachments/assets/9f49918d-e9f8-4c47-90eb-58fec249ae5d)

**Actual Output:**

![image](https://github.com/user-attachments/assets/ef3d26ed-9341-4a49-b992-744e0ef620a7)

### Test 4

Setelah customer selesai berbelanja, mereka akan menghitung total beanja yang harus dibayarkan menggunakan method 
total_price(). Sebelum mengeluarkan output, method akan menampilkan item-item yang dibeli.

**Expected Output:**

![image](https://github.com/user-attachments/assets/7dce32f0-9759-4cd8-a8b6-54ef889ac44c)

**Actual Output:**

![image](https://github.com/user-attachments/assets/443b1e17-5292-468a-bc36-3c9e12ac43c5)

## Conclusion

Semua fitur yang menjadi objectives dalam pembuatan sistem self cashier PacMart telah berfungsi dengan baik untuk meningkatkan efisiensi proses
bisnis supermarket yang dimiliki oleh Andi. Adapun pengembangan yang dapat dilakukan pada sistem ini adalah:

- Mengintegrasikan sistem dengan database yang dapat menyimpan semua informasi transaksi secara utuh.
- Menyediakan preferensi pemilihan bahasa selain bahasa Indonesia, mengingat supermarket yang dimiliki Andi berskala besar yang memungkinkan konsumen berasal dari luar negara Indonesia.

## Contact

Created by Bagaskoro Adi Hutomo
Email: bagaskoroah@gmail.com
Feel free for any further discussion! :)
