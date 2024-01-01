import os
import json

data_uang = []


def tampilan_awal():
    print('='*55)
    print('='*10, 'Selamat Datang Di Aplikasi E-Note', '='*10)
    print('='*55,)
    print('Pilih Menu:')
    print('1. Register')
    print('2. Login')
    print('3. Logout')
    print('='*55)
    print('Pilih Menu Yang Ingin Digunakan')
    masuk = int(input('> '))
    if masuk == 1 :
        register()
    elif masuk == 2 :
        login()
    elif masuk == 3 :
        logout()
    else:
        salah_awal()

def buat_file(nama_file, data):
    with open(f"{nama_file}.json", "w") as f:
        json.dump(data, f, indent=6)

def baca_file(namaFile):
    with open(f"{namaFile}.json", "r") as f:
        return json.load(f)

def register():
    os.system('cls')
    print('='*10, 'Silahkan Melakukan Registrasi', '='*10)
    print()
    global username
    username = input('Daftarkan Username Anda: ')
    password = input('Daftarkan Password Anda: ')

    data = {
    "username": username,
    "password": password,
    }

    try:
        buat_file('data_login', data)
        print('Registrasi Berhasil. . . ')
        tampilan_awal()
    except:
        print('Registrasi Gagal. . .')
        tampilan_awal()

def login():
    os.system('cls')
    print('='*10, 'Silahkan Melakukan Login', '='*10)
    read = baca_file('data_login')
    uname = input("Masukkan Username Anda: ")
    pw = input("Masukkan Password Anda: ")

    if read ['username'] == uname and read['password'] == pw:
        os.system('cls')
        print('Login Berhasil. . .')
        menu()
    else:
        os.system('cls')
        print('Gagal Melakukan Login. . .')
        tampilan_awal()

def logout():
    os.system('cls')
    print('Berhasil Logout. . .')

def salah_awal():
    os.system('cls')
    print('Masukan Menu Dengan Benar')
    tampilan_awal()
#-----------------------------------------------------------------------------------------------------------
def menu():
    print('='*81)
    print('='*20, 'Selamat Datang Di Aplikasi E-Note', '='*26)
    print('='*81,)
    print('1. Cek Saldo Saat Ini')  
    print('2. Masukkan Pemasukan Keuangan')
    print('3. Masukkan Pengeluaran Keuangan')
    print('4. Cetak Catatan Keuangan')
    print('5. Hapus Catatan Keuangan')
    print('6. Logout')
    print('='*81)
    
    pilih = int(input('Pilih Menu Yang Ingin Digunakan: '))
    if pilih == 1 :
        saldo()
    elif pilih == 2 :
        pemasukan()
    elif pilih == 3 :
        pengeluaran()
    elif pilih == 4 :
        cetak()
    elif pilih == 5 :
        hapus()
    elif pilih == 6 :
        finish()
    else:
        salah()
# _________________________________Cek Saldo__________________________________
def saldo() :
    os.system('cls')
    print('-'*10, 'Saldo Anda Saat Ini', '-'*10)
    read = baca_file('data_utama')
    try:    
        total_dana = 0
        for i in range(len(read)):
            total_dana+= read[i]['jumlah']
        print('> Saldo Anda : Rp.', total_dana)

    except:
        print('gagal membaca')

    back()
    menu()

# _________________________________Pemasukan__________________________________
def pemasukan():  
    jenis_transaksi = 'Pemasukan' 
    global username
    uang_masuk = int(input('Jumlah Pemasukan: Rp. '))
    with open('data_utama.json','r') as see:
        forsaldo = json.load(see)
    if len(forsaldo) > 1: 
        tambah_total = uang_masuk + forsaldo[-1]['total saldo']
    else :
        tambah_total = uang_masuk
    catatan = input('Tambahkan Catatan Pemasukan: ')
    try:
        isi = { 
            'nama' : username,  
            'jenis transaksi' : jenis_transaksi, 
            'jumlah' : uang_masuk,
            'total saldo' : tambah_total,
            'catatan' : catatan,
        }  
        try:
            data_uang.append(isi)
            buat_file('data_utama', data_uang) 
            os.system('cls')
            print('Berhasil ditambahkan. . .')
            back()
            menu()
        except:
            print('gagal')
            enter = input()
    except:
        print('gagal membuat')
        enter = input()
        menu()
        back()
# _________________________________Pemasukan selesai__________________________________

# _________________________________Pengeluaran_________________________________
def pengeluaran():
    global username
    jenis_transaksi = 'Pengeluaran'
    awal = int(input('Jumlah Pengeluaran: Rp. ')) 
    uang_keluar = awal*-1 
    catatan = input('Catatan Pengeluaran: ')
    with open('data_utama.json','r') as see:
        forsaldo = json.load(see)
    if len(forsaldo) > 1: 
        kurang_total =  forsaldo[-1]['total saldo'] + uang_keluar 
    else :
        kurang_total = uang_keluar

    try:
        isi = {  
            'nama' : username,
            'jenis transaksi' : jenis_transaksi, 
            'jumlah' : uang_keluar, 
            'total saldo' : kurang_total,  
            'catatan' : catatan
            }
        try:
            data_uang.append(isi) 
            buat_file('data_utama', data_uang) 
            os.system('cls')
            print('Berhasil ditambahkan!')
            back()
            menu()
        except:
            print('gagal')
    except:
        print('gagal membuat')
    print('masuk')
    menu()

# _________________________________Pengeluaran selesai__________________________________

# _________________________________Cetak keuangan__________________________________

def cetak():
    os.system('cls')
    print('='*65)
    print('='*21, 'Catatan Keuangan Anda', '='*21)
    print('='*65)
    read = baca_file('data_utama')
    print(f"{'Nama': ^7}{'Jenis Transaksi': ^12}{'Jumlah': ^15}{'Total Saldo': ^13}{'Keterangan': ^15}")
    print('-'*65)
    try:    
        total_dana = 0
        for i in range(len(read)):
            total_dana+= read[i]['jumlah']
            print(f"{read[i]['nama']: ^5}{read[i]['jenis transaksi']: ^17} {read[i]['jumlah']: ^12} {total_dana: ^12} {read[i]['catatan']: ^15}")
            print('-'*65)
        
        back()
        os.system('cls')
        menu()
    except:
        print('gagal membaca')

# _________________________________Cetak keuangan selesai__________________________________

# _________________________________Hapus__________________________________

def hapus() :
    baca = baca_file('data_utama')
    print(f"{'Nama': ^7}{'Jenis Transaksi': ^12}{'Jumlah': ^15}{'Total Saldo': ^13}{'Keterangan': ^15}")
    print('-'*65)
    try:    
        total_dana = 0
        for i in range(len(baca)):
            total_dana+= baca[i]['jumlah']
            print(f"{baca[i]['nama']: ^5}{baca[i]['jenis transaksi']: ^17} {baca[i]['jumlah']: ^12} {total_dana: ^12} {baca[i]['catatan']: ^15}")
            print('-'*65)
        print('Pilih Baris Yang Ingin Dihapus:')
        perintah = int(input('> '))
        rmv = baca[perintah-1]
        baca.remove(rmv)
        with open ('data_utama.json', 'w') as update :
            json.dump(baca, update)
        os.system('cls')
        print('Berhasil Menghapus Data. . .')
        menu()
    except:
        print('gagal membaca')

    
def salah():
    os.system('cls')
    print('Masukan Pilihan Menu Dengan Benar')
    print()
    menu()

def back(): 
    input('Tekan enter untuk kembali ke menu') 

def finish():
    os.system('cls')
    print('Berhasil Logout. . .')

tampilan_awal()
