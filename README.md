# PacMart: Self Service Cashier

Self-Service Cashier adalah program kasir sederhana berbasis Python yang memungkinkan pelanggan mencatat, mengubah, dan menghitung transaksi belanja mereka secara mandiri. 
Program ini cocok untuk simulasi sistem kasir mandiri (self-checkout) dengan fitur yang interaktif dan dinamis.

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

## Code Flow Explanation


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
📧 Email: bagaskoroah@gmail.com
Feel free for any further discussion! :)
