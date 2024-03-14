import random 
from Function import WelcomeMessage

WelcomeMessage ("WELCOME TO VASA GAMES!!")

nama = input("Masukkan nama Anda: ") 
while nama == "":
    nama = input("Isi dulu biar makin Kenal: ")
    
while True:
    Bentuk_Rumah = "|__|"
    Rumah_Kosong = [Bentuk_Rumah] * 3
    Rumah_Ayang = Rumah_Kosong.copy()

    AYANGKU_posisi = random.randint(1, 3)
    Rumah_Ayang[AYANGKU_posisi - 1] = "|_<3_|"

    Rumah_Kosong = ' '.join(Rumah_Kosong)
    Rumah_Ayang = ' '.join(Rumah_Ayang)
    
    print(f'''
    Halo {nama}! Coba perhatikan Rumah Kost ini
    {Rumah_Kosong}
    ''')

    pilihan = int(input("Menurut kamu di Rumah manakah AYANGKU berada? [1 / 2 / 3]: "))
    while pilihan > 3:
        pilihan = int(input("Pilih Rumah yang tersedia: "))
        print(f"Okei, Rumah {pilihan} tersedia")
        
        
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
        
    main_lagi = input("\nApakah Anda ingin menebak lagi? [y/n]: ")
    if main_lagi == "n":
        break
    
print("Permainan menebaknya sudah selesai!! Terima Kasih sudah bermain!!")