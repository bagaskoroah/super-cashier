from tabulate import tabulate

class Transaction:
  """
  Kelas untuk mengelola informasi transaksi belanja melalui sistem kasir self-service dengan fitur menambah, mengubah informasi, menghapus, dan menampilkan item.
  """
  def __init__(self):
    """Inisialisasi objek yang merupakan dictionary kosong yang nantinya digunakan untuk menyimpan item transaksi."""
    self.items = dict() # Menyimpan data informasi transaksi dengan format {nama_item: [jumlah_item, harga_item]}

  def add_item(self):
    """Menambahkan item ke dalam daftar transaksi."""
    while True:
      try:
        self.item_name = input('Masukkan nama item: ')
        if self.item_name.isdigit():
          raise ValueError('Nama item tidak boleh berupa angka!')

        self.item_qty = input('Masukkan jumlah item: ')
        self.item_price = input('Masukkan harga item: ')
        if not self.item_qty.isdigit() or not self.item_price.isdigit():
          raise ValueError('Jumlah item atau harga item yang dimasukkan harus berupa angka!')

        # Menambah item baru dengan format kapital dan menghapus input whitespace
        self.items[self.item_name.strip().title()] = [int(self.item_qty), int(self.item_price)]

        while True:
          # Menanyakan pada user apakah ingin menambah item lain atau kembali pada main menu untuk melakukan aktivitas lain
          option = input('\nApakah anda ingin melanjutkan pencatatan transaksi? Ketik "Ya" untuk melanjutkan dan "Tidak" untuk berhenti serta mencetak informasi transaksi Anda: ')
          if option in ['Ya', 'YA', 'ya', 'yA']:
            break
          elif option in ['Tidak', 'tidak', 'TIDAK']:
            return
          else:
            print('\nFormat input option tidak sesuai! Silakan input "Ya" untuk melanjutkan dan "Tidak" untuk berhenti serta mencetak informasi transaksi Anda!')
      
      except ValueError as e:
        # Menampilkan pesan error pada input yang tidak valid
        print(f'Error: {e}. Silakan coba lagi sesuai dengan format yang diminta!\n')

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
    name_target = input('Masukkan nama item yang ingin diubah jumlahnya: ')
    for key, value in self.items.items():
      if name_target == key:
        # Update jumlah item barang
        value[0] = int(input('Masukkan jumlah item yang baru: '))

    return self.items

  def update_item_price(self):
    """Mengubah nominal harga item pada daftar transaksi."""
    name_target = input('Masukkan nama item yang ingin diubah harganya: ')
    for key, value in self.items.items():
      if name_target == key:
        # Update harga item barang
        value[1] = int(input('Masukkan nominal harga yang baru: '))

    return self.items

  def delete_item(self):
    """Menghapus item tertentu dari daftar transaksi berdasarkan nama item."""
    item_to_delete = input('Masukkan nama item yang ingin dihapus dari daftar transaksi: ').strip()
    if item_to_delete in self.items:
      self.items.pop(item_to_delete) # Menghapus item tertentu dari dictionary
    else:
      print('Item tidak ditemukan dalam daftar transaksi!')

  def reset_transaction(self):
    """Menghapus semua item dalam daftar transaksi."""
    self.items.clear() # Mengosongkan semua key-value pada dictionary

    print('\nSemua item berhasil di delete!')

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

  def total_price(self):
    """Menampilkan total harga transaksi serta potongannya apabila memenuhi syarat diskon berdasarkan total harga."""
    total_transaction = 0

    for key, value in self.items.items():
      total_transaction += value[0] * value[1] # Menghitung total harga berdasarkan jumlah item * harga/item

    if '' in self.items:
      order_list = [(key, value[0], value[1], value[0] * value[1]) for key, value in self.items.items()]
      headers = ['Nama Item', 'Jumlah Item', 'Harga/Item', 'Total Harga']
      print('Format item kamu masih kurang tepat atau ada yang belum terisi, silakan lengkapi terlebih dahulu!\n')
      print(tabulate(order_list, headers=headers))

    elif total_transaction <= 200000:
      print(f'\nItem yang dibeli adalah {self.items}')
      print(f'Total belanja yang harus dibayarkan adalah Rp. {total_transaction}')

    elif 200000 < total_transaction <= 300000:
      disc = 0.05
      total_transaction -= total_transaction*disc
      print(f'\nItem yang dibeli adalah {self.items}')
      print(f'Total belanja yang harus dibayarkan adalah Rp. {total_transaction}')

    elif 300000 < total_transaction <= 500000:
      disc = 0.08
      total_transaction -= total_transaction*disc
      print(f'\nItem yang dibeli adalah {self.items}')
      print(f'Total belanja yang harus dibayarkan adalah Rp. {total_transaction}')

    elif total_transaction > 500000:
      disc = 0.10
      total_transaction -= total_transaction*disc
      print(f'\nItem yang dibeli adalah {self.items}')
      print(f'Total belanja yang harus dibayarkan adalah Rp. {total_transaction}')

    