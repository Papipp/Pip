import json # fungsinya untuk membaca dan menulis data dalam format JSON
import os   # fungsinya untuk berinteraksi dengan sistem operasi
import random #fungsinya untuk menghasilkan angka acak

# Fungsi untuk membaca data
def baca_data():
    if not os.path.exists("Data_pengguna.json"): # fungsi os.path.exist digunakan untuk mengecek apakah file sudah ada atau belum
        return {}
    with open("Data_pengguna.json", "r") as file:
        return json.load(file) # json.load digunakan untuk membaca file JSON

# Fungsi untuk menyimpan data
def simpan_data(data):
    with open("Data_pengguna.json", "w") as file: # Digunakan buat menulis data
        json.dump(data, file, indent=4) # json.dump digunakan untuk menulis data e file JSON

# Database pengguna
users = baca_data() 

# Fungsi login
def login():
    print("=== BMU Mobile ===")
    print("________LOGIN_________")
    print(" "),
    username = input("Masukkan username : ")
    if username in users:
        for _ in range(3):
            pin = input("Masukkan PIN : ")
            if pin == users[username]["pin"]:
                print(" ")
                print(f"Login berhasil. Selamat datang, {username}!\n")
                return username
            else:
                print("PIN salah. Silakan coba lagi.")
        print("Anda telah salah memasukkan PIN sebanyak 3 kali. Akun terkunci.")
    else:
        print("Username tidak ditemukan.")
    return None

# Fungsi untuk cek saldo
def cek_saldo(username):
    saldo = users[username]["saldo"] # Ambil saldo dari database
    print(f"Saldo Anda: Rp{saldo:,}\n")

# Fungsi untuk transfer
def transfer(username):
    tujuan = input("Masukkan username tujuan: ")
    if tujuan in users and tujuan != username:
        try:
            jumlah = int(input("Masukkan jumlah transfer : Rp"))
            if jumlah > 0 and jumlah <= users[username]["saldo"]:
                users[username]["saldo"] -= jumlah 
                users[tujuan]["saldo"] += jumlah
                simpan_data(users)  # Simpan perubahan ke file
                print(f"Transfer berhasil. Anda telah mentransfer Rp{jumlah:,} ke {tujuan}.\n")
            else:
                print("Saldo tidak cukup atau jumlah tidak valid !!!\n")
        except ValueError:
            print("Masukkan jumlah transfer yang valid !!!\n")
    else:
        print("Username tujuan tidak valid !!!\n")

# Fungsi Tarik tunai
def tarik_tunai(username):
    try:
        jumlah = int(input("Masukkan jumlah tarik tunai: Rp"))
        if jumlah > 0 and jumlah <= users[username]["saldo"]:
            # menghasilkan kode acak
            kode_acak = random.randint(100000, 999999) 
            print(f"Kode verifikasi: {kode_acak}")
            
            # input kode verifikasi
            kode_input = input("Masukkan kode verifikasi: ")
            if kode_input == str(kode_acak):
                users[username]["saldo"] -= jumlah
                simpan_data(users)  # Simpan perubahan ke file
                print(f"Tarik tunai berhasil. Anda menarik Rp{jumlah:,}.\n")
            else:
                print("Kode verifikasi salah. Tarik tunai dibatalkan.\n")
        else:
            print("Saldo tidak cukup atau jumlah tidak valid !!!\n")
    except ValueError:
        print("Masukkan jumlah tarik tunai yang valid !!!\n")

# Menu utama
def main_menu(username):
    while True:
        print("=== Menu Utama ===")
        print("1. Cek Saldo")
        print("2. Transfer")
        print("3. Tarik Tunai")
        print("4. Keluar")
        Pilihan = input("Pilih menu : ")
        
        if Pilihan == "1":
            cek_saldo(username)
        elif Pilihan == "2":
            transfer(username)
        elif Pilihan == "3":
            tarik_tunai(username)
        elif Pilihan == "4":
            print("Terima kasih telah menggunakan Mobile Banking.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Fungsi utama
def main(): 
    username = login() 
    if username:
        main_menu(username) 

if __name__ == "__main__":
    # Inisialisasi data awal jika file kosong
    if not users:
        users = {
            "Papipp": {"pin": "123456", "saldo": 500000},
            "Awalisani": {"pin": "111111", "saldo": 500000},
            "Avrila": {"pin": "222222", "saldo": 500000}
        }
        simpan_data(users)
    
    main()
