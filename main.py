from script import Transaction

def main():
    transaksi = Transaction()

    while True:
        print("\n--- SELAMAT DATANG DI PACMART ---")
        print("1. Tambah Item")
        print("2. Ubah Nama Item")
        print("3. Ubah Jumlah Item")
        print("4. Ubah Harga Item")
        print("5. Hapus Item")
        print("6. Reset Transaksi")
        print("7. Cek Daftar Transaksi")
        print("8. Hitung Total Harga")
        print("9. Keluar")

        try:
            pilihan = int(input("\nPilih menu (1-9): "))
            if pilihan == 1:
                transaksi.add_item()
            elif pilihan == 2:
                transaksi.update_item_name()
            elif pilihan == 3:
                transaksi.update_item_qty()
            elif pilihan == 4:
                transaksi.update_item_price()
            elif pilihan == 5:
                transaksi.delete_item()
            elif pilihan == 6:
                transaksi.reset_transaction()
            elif pilihan == 7:
                transaksi.check_order()
            elif pilihan == 8:
                transaksi.total_price()
            elif pilihan == 9:
                print("\nTerima kasih telah berbelanja di PacMart!")
                break
            else:
                print("Pilihan tidak valid. Masukkan angka 1-9.")
        except ValueError:
            print("Input harus berupa angka.")

if __name__ == '__main__':
    main()