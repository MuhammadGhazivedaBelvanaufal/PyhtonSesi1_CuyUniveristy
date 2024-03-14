import random
import Sesi4
 

def game():
    while True:
        Bentuk_Rumah = "|__|"
        Rumah_Kosong = [Bentuk_Rumah] * 3
        Rumah_Ayang = Rumah_Kosong.copy()

        AYANGKU_posisi = random.randint(1, 3)
        Rumah_Ayang[AYANGKU_posisi - 1] = "|_<3_|"

        Rumah_Kosong = ' '.join(Rumah_Kosong)
        Rumah_Ayang = ' '.join(Rumah_Ayang)
        
        print(f'Coba perhatikan Rumah Kost ini\n\n{Rumah_Kosong}\n')

        pilihan = int(input("Menurut kamu di Rumah manakah AYANGKU berada? [1 / 2 / 3]: "))
        while pilihan > 3:
            pilihan = int(input("Pilih Rumah yang tersedia: "))
            print(f"Okei, Rumah {pilihan} tersedia")
        if pilihan == AYANGKU_posisi:
            print("=============================================================================")
            print(f"{Rumah_Ayang} HOREEEE!! Kamu benar menebak posisi AYANGKU!!")
            print("=============================================================================")
        else:
            print("=============================================================================")
            print(f"{Rumah_Ayang} NOOOOOO!! Kamu salah menebak posisi AYANGKU!!")
            print("=============================================================================")
            
        main_lagi = input("\nApakah Anda ingin menebak lagi? [y/n]: ")
        if main_lagi != "y":
            Sesi4.Menu()
    
if __name__ == '__main__':
    game()