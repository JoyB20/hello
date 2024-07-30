# Program aritmatika 
# 1. Hitung kecepatan
# 2. Hitung jarak
# 3. Hitung waktu
# 4. Hitung luas persegi panjang
# 5. Hitung luas segitiga
# 6. EXIT

# Mendeklarasikan fungsi 

def hitung_kecepatan():
    jarak = int(input('Masukkan jarak: '))
    waktu = int(input('Masukkan waktu: '))
    kecepatan = jarak / waktu # Rumus menghitung kecepatan
    print('Kecepatan: ', kecepatan, 'km/jam')

    # Setelah melakukan hitung kecepatan, akan muncul kalimat pada layar 
    # seperti, "Selamat anda menghitung kecepatan!" sebanyak 5x
    # Kita akan menggunakan while loop pada bagian ini

    # Deklarasi while loop

    nilai_awal = 0
    nilai_akhir = 5 # Opsional

    while nilai_awal < nilai_akhir:
        print('Selamat anda menghitung kecepatan!')
        nilai_awal = nilai_awal + 1 # Setelah kalimat muncul di layar, otomatis nilai dari variable nilai awal akan bertambah/increment
    print('\n') 

def hitung_jarak():
    kecepatan = int(input('Masukkan kecepatan: '))
    waktu = int(input('Masukkan waktu: '))
    jarak = kecepatan * waktu # Rumus menghitung kecepatan 
    print('Jarak: ', jarak, 'km')

    # Setelah melakukan hitung kecepatan, akan muncul kalimat pada layar 
    # seperti, "Selamat anda menghitung jarak!" sebanyak 5x
    # Kita akan menggunakan while loop pada bagian ini

    # Deklarasi while loop

    nilai_awal = 0
    nilai_akhir = 5 # Opsional

    while nilai_awal < nilai_akhir:
        print('Selamat anda menghitung jarak!')
        nilai_awal = nilai_awal + 1 # Setelah kalimat muncul di layar, otomatis nilai dari variable nilai awal akan bertambah/increment
    print('\n')

def hitung_waktu():
    jarak = int(input('Masukkan jarak: '))
    kecepatan = int(input('Masukkan kecepatan: '))
    waktu = jarak/kecepatan # Rumus menghitung waktu
    print('Waktu: ', waktu, 'jam')

    # Setelah melakukan hitung kecepatan, akan muncul kalimat pada layar 
    # seperti, "Selamat anda menghitung waktu!" sebanyak 5x
    # Kita akan menggunakan while loop pada bagian ini

    # Deklarasi while loop

    nilai_awal = 0
    nilai_akhir = 5 # Opsional

    while nilai_awal < nilai_akhir:
        print('Selamat anda menghitung waktu!')
        nilai_awal = nilai_awal + 1 # Setelah kalimat muncul di layar, otomatis nilai dari variable nilai awal akan bertambah/increment
    print('\n')

def hitung_luas_persegi_panjang():
    panjang = int(input('Masukkan panjang: '))
    lebar = int(input('Masukkan lebar: '))
    luas = panjang * lebar # Rumus menghitung luas persegi panjang
    print('Luas: ', luas, 'cm')

    # Setelah melakukan hitung kecepatan, akan muncul kalimat pada layar 
    # seperti, "Selamat anda menghitung luas persegi panjang!" sebanyak 5x
    # Kita akan menggunakan while loop pada bagian ini

    # Deklarasi while loop

    nilai_awal = 0
    nilai_akhir = 5 # Opsional

    while nilai_awal < nilai_akhir:
        print('Selamat anda menghitung luas persegi panjang!')
        nilai_awal = nilai_awal + 1 # Setelah kalimat muncul di layar, otomatis nilai dari variable nilai awal akan bertambah/increment
    print('\n')

def hitung_luas_segitiga():
    alas = int(input('Masukkan alas: '))
    tinggi = int(input('Masukkan tinggi: '))
    luas =  alas * tinggi / 2 # Rumus menghitung luas segitiga
    print('Luas: ', luas, 'cm')

    # Setelah melakukan hitung kecepatan, akan muncul kalimat pada layar 
    # seperti, "Selamat anda menghitung luas segitiga!" sebanyak 5x
    # Kita akan menggunakan while loop pada bagian ini

    # Deklarasi while loop

    nilai_awal = 0
    nilai_akhir = 5 # Opsional

    while nilai_awal < nilai_akhir:
        print('Selamat anda menghitung luas segitiga ')
        nilai_awal = nilai_awal + 1 # Setelah kalimat muncul di layar, otomatis nilai dari variable nilai awal akan bertambah/increment
    print('\n')
          
# Kita akan membuat sebuah fungsi, dimana jika pengguna hanya klik tombol "enter" saat diberi pilihan
# maka akan tampil pada laya sebuah pesan peringatan seperti, "Isi dulu" hingga pengguna melakukan
# sesuai yang telah diperintahkan

#def input_kosong(pilihan_pengguna):
#   while pilihan_pengguna == '':
#       pilihan_pengguna = input('Isi dulu: ')

# Bagian ini merupakan mekanisme utama program. Pada bagian ini tentu saja kita akan menggunakan
# if-else statement di dalam sebuah while loop, agar setelah pengguna dapat menggunakan pilihan
# secara terus menerus, terkecuali jika pengguna memilih untuk "EXIT"

while True:
    print(f'''   .-'-.
       /`     |__
     /`  _.--`-,-`         
     '-|`   a '<-.   []    with Sir Popeye
       \     _\__) \=`     
        C_  `    ,_/       
jgs       | ;----'         
 ''') # Bagian ini akan berisi ascii
    pilihan_pengguna = input('Program Aritmatika \n 1. Hitung Kecepatan \n 2. Hitung Jarak \n 3. Hitung Waktu \n 4. Hitung Luas Persegi Panjang \n 5. Hitung Luas Segitiga \n \n 6. EXIT \n Masukkan pilihan: ')
    print('\n')

    #If-else statement atau switch case

    if pilihan_pengguna == '':
        while pilihan_pengguna == '':
            pilihan_pengguna = input('Isi dulu: ')
            if pilihan_pengguna == '1':
                hitung_kecepatan()
            elif pilihan_pengguna == '2':
                hitung_jarak()
            elif pilihan_pengguna == '3':
                hitung_waktu()
            elif pilihan_pengguna == '4':
                hitung_luas_persegi_panjang()
            elif pilihan_pengguna == '5':
                hitung_luas_segitiga()
            elif pilihan_pengguna == '6':
                exit()
    elif pilihan_pengguna == '1':
        hitung_kecepatan()
    elif pilihan_pengguna == '2':
        hitung_jarak()
    elif pilihan_pengguna == '3':
        hitung_waktu()
    elif pilihan_pengguna == '4':
        hitung_luas_persegi_panjang()
    elif pilihan_pengguna == '5':
        hitung_luas_segitiga()
    elif pilihan_pengguna == '6':
        exit()

# Langit
