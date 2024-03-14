import random 

WelcomeMessage = "WELCOME TO VASA GAMES!!"
AYANGKU_posisi = random.randint(1, 3)

print("=============================")
print(f"** {WelcomeMessage} **")
print("=============================")

nama = input("Masukkan nama Anda: ")

Bentuk_Rumah = "|__|"
Rumah_Kosong = [Bentuk_Rumah] * 3
Rumah_Ayang = Rumah_Kosong.copy()

Rumah_Ayang[AYANGKU_posisi - 1] = "|<3|"

print(f'''
Halo {nama}! Coba perhatikan Rumah Kost ini
{Rumah_Kosong}
''')

pilihan = int(input("Menurut kamu di Rumah manakah AYANGKU berada? [1 / 2 / 3]: "))
confirm = input("Konfimasi pilihan Anda [Yakin/Tidak]: ")
if confirm == "Yakin":
    if pilihan == AYANGKU_posisi:
        print("=============================================================================")
        print(f"{Rumah_Ayang} HOREEEE {nama}!! Kamu benar menebak posisi AYANGKU!!")
        print("=============================================================================")
    else:
        print("=============================================================================")
        print(f"{Rumah_Ayang} NOOOOOO {nama}!! Kamu salah menebak posisi AYANGKU!!")
        print("=============================================================================")
elif confirm == "Tidak":
    print("======================================================")
    pilihan = int(input("Pilih dengan keyakinan penuh kali ini!! [1 / 2 / 3]: "))
    confirm = input("Konfimasi pilihan Anda [Yakin/Tidak]: ")
    print("======================================================")
    if confirm == "Yakin":
        if pilihan == AYANGKU_posisi:
            print("=============================================================================")
            print(f"{Rumah_Ayang} HOREEEE {nama}!! Kamu benar menebak posisi AYANGKU!!")
            print("=============================================================================")
        else:
            print("=============================================================================")
            print(f"{Rumah_Ayang} NOOOOOO {nama}!! Kamu salah menebak posisi AYANGKU!!")
            print("=============================================================================")
    elif confirm == "Tidak":
        print("======================================================")
        pilihan = int(input("Kesempatan terakhir untuk memilih Rumah Kost AYANGKU berada!! [1 / 2 / 3]: "))
        confirm = input("Konfimasi pilihan Anda [Yakin/Tidak]: ")
        print("======================================================")
        if confirm == "Yakin":
            if pilihan == AYANGKU_posisi:
                print("=============================================================================")
                print(f"{Rumah_Ayang} HOREEEE {nama}!! Kamu benar menebak posisi AYANGKU!!")
                print("=============================================================================")
            else:
                print("=============================================================================")
                print(f"{Rumah_Ayang} NOOOOOO {nama}!! Kamu salah menebak posisi AYANGKU!!")
                print("=============================================================================")
        else:
            print("VASA GAMES Diberhentikan!! Silahkan Mulai Program Kembali!!")
    else:
        print("VASA GAMES Diberhentikan!! Silahkan Mulai Program Kembali!!")
else:
    print("VASA GAMES Diberhentikan!! Silahkan Mulai Program Kembali!!")