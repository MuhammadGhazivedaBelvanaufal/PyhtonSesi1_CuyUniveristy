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
| |  | |  | |
|_|  |_|  |_|

''')

pilihan = int(input("Menurut kamu di Rumah manakah AYANGKU berada? [1 / 2 / 3]: "))

if pilihan == AYANGKU_posisi:
    print(f"SELAMAT {nama}!! Kamu benar menebak posisi AYANGKU!! posisi AYANGKU ada di {AYANGKU_posisi} dan pilihanmu adalah Rumah No.{pilihan}")
else:
    print(f"COBALAGI {nama}!! Kamu salah menebak posisi AYANGKU!! posisi AYANGKU ada di {AYANGKU_posisi} dan pilihanmu adalah Rumah No.{pilihan}")