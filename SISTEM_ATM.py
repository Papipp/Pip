 # Fungsi baca database
def read_data():
    akunatm = {}
    try:
        with open('database_atm.txt', 'r') as file:
            for line in file:
                id_akun, saldo = line.strip().split(',')
                akunatm[id_akun] = {'saldo': float(saldo)}
    except FileNotFoundError:
        pass 
    return akunatm

# Fungsi menulis isi database
def write_data(data):
    with open('database_atm.txt', 'w') as file:
        for id_akun, info_saldo in data.items(): 
            file.write(f"{id_akun}, {info_saldo['saldo']}\n")

# Fungsi untuk menampilkan menu
def pilihan_menu():
    print("====== ATM ======")
    print("=pilih Transaksi=")
    print("1. Cek Saldo") 
    print("2. Setor Uang")
    print("3. Tarik Uang")
    print("4. Keluar")
    print("=================")

# Fungsi cek saldo
def cek_saldo(rek):
    print(f"Saldo Rekening Anda : {rek['saldo']}")

# Fungsi setor uang
def setor_uang(rek):
    while True:
        try:
            jumlah = float(input("Masukkan jumlah uang yang ingin disetor : "))
            if jumlah <= 0:
                print("Jumlah harus lebih besar dari 0.")
                continue
            rek['saldo'] += jumlah
            print(f"Anda telah menyetor : {jumlah}")
            print(f"Saldo Rekening Anda sekarang adalah : {rek['saldo']}")
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

# Fungsi tarik uang
def tarik_uang(rek):
    while True:
        try:
            jumlah = float(input("Masukkan jumlah uang yang ingin ditarik : "))
            if jumlah <= 0:
                print("Jumlah harus lebih besar dari 0.")
                continue
            if jumlah > rek['saldo']:
                print("Saldo Rekening Anda tidak cukup!")
            else:
                rek['saldo'] -= jumlah
                print(f"Anda telah menarik: {jumlah}")
                print(f"Saldo Rekening Anda sekarang: {rek['saldo']}")
                break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

# Fungsi utama sistem ATM
def sistem_atm():
    # Membaca data pengguna
    akunatm = read_data()
    
    # Input ID akun
    id_akun = input("Masukkan ID Akun Anda: ")
    
    # Jika akun tidak ada, buat akun baru
    if id_akun not in akunatm:
        akunatm[id_akun] = {'saldo': 0}
        print("Akun baru telah dibuat.")
    
    rek = akunatm[id_akun]

    while True:
        pilihan_menu()
        pilihan = input("Pilih Transaksi (1-4): ")

        if pilihan == '1':
            cek_saldo(rek)
        elif pilihan == '2':
            setor_uang(rek)
        elif pilihan == '3':
            tarik_uang(rek)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan ATM!")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih antara 1-4.")

    # Menyimpan data kembali ke file databse
    write_data(akunatm)

# Menjalankan sistem ATM
if __name__ == "__main__":
    sistem_atm()