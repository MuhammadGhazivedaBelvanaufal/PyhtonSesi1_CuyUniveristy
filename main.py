# nama = "belvanaufal"
# pacar = "susan"
# usia = 19

# print("*             *")
# print("* " + nama + " *")
# print(f"**** {pacar} ****")
# print("*             *") 

# print(f'''
# nama saya adalah {nama}
# usia saya adalah {usia}
#       ''')
# **************************************
# PacarSaya = "Susan"

# if PacarSaya == "wimala":
#     print("Kamu selingkuh")
# if PacarSaya == "Susan":
#     print("Kamu setia")
# else:
#     print("Kamu Playboy")
import random 

WelcomeMessage = "WELCOME TO VASA GAMES!!"
AYANGKU_posisi = random.randint(1, 3)

print("*****************************")
print(f"** {WelcomeMessage} **")
print("*****************************")

nama = input("Masukkan nama Anda: ")

print(f'''
Halo {nama}! Coba perhatikan Rumah Kost ini
 _    _    _
/ \  / \  / \ 
|_|  |_|  |_|

''')

pilihan = int(input("Menurut kamu di Rumah manakah AYANGKU berada? [1 / 2 / 3]: "))
confirm = input("Konfimasi pilihan Anda [Yakin/Tidak]: ")
if confirm == "Yakin":
    if pilihan == AYANGKU_posisi:
        print("**************************************************************************************************************************")
        print(f"SELAMAT {nama}!! Kamu benar menebak posisi AYANGKU!! Posisi AYANGKU ada di {AYANGKU_posisi} dan pilihanmu adalah Rumah No.{pilihan}")
        print("**************************************************************************************************************************")
    else:
        print("**************************************************************************************************************************")
        print(f"COBALAGI {nama}!! Kamu salah menebak posisi AYANGKU!! Posisi AYANGKU ada di {AYANGKU_posisi} dan pilihanmu adalah Rumah No.{pilihan}")
        print("**************************************************************************************************************************")
elif confirm == "Tidak":
    print("******************************************************")
    pilihan = int(input("Pilih dengan keyakinan penuh kali ini!! [1 / 2 / 3]: "))
    confirm = input("Konfimasi pilihan Anda [Yakin/Tidak]: ")
    print("******************************************************")
    if confirm == "Yakin":
        if pilihan == AYANGKU_posisi:
            print("**************************************************************************************************************************")
            print(f"SELAMAT {nama}!! Kamu benar menebak posisi AYANGKU!! Posisi AYANGKU ada di {AYANGKU_posisi} dan pilihanmu adalah Rumah No.{pilihan}")
            print("**************************************************************************************************************************")
        else:
            print("**************************************************************************************************************************")
            print(f"COBALAGI {nama}!! Kamu salah menebak posisi AYANGKU!! Posisi AYANGKU ada di {AYANGKU_posisi} dan pilihanmu adalah Rumah No.{pilihan}")
            print("**************************************************************************************************************************")
    else:
        print("******************************************************")
        pilihan = int(input("Kesempatan terakhir untuk memilih Rumah Kost AYANGKU berada!! [1 / 2 / 3]: "))
        confirm = input("Konfimasi pilihan Anda [Yakin/Tidak]: ")
        print("******************************************************")
        if confirm == "Yakin":
            if pilihan == AYANGKU_posisi:
                print("**************************************************************************************************************************")
                print(f"SELAMAT {nama}!! Kamu benar menebak posisi AYANGKU!! Posisi AYANGKU ada di {AYANGKU_posisi} dan pilihanmu adalah Rumah No.{pilihan}")
                print("**************************************************************************************************************************")
            else:
                print("**************************************************************************************************************************")
                print(f"COBALAGI {nama}!! Kamu salah menebak posisi AYANGKU!! Posisi AYANGKU ada di {AYANGKU_posisi} dan pilihanmu adalah Rumah No.{pilihan}")
                print("**************************************************************************************************************************")
else:
    print("VASA GAMES Diberhentikan!! Silahkan Mulai Program Kembali!!")
