import Sesi4

def shop():
    while True:
        print("ini shop kita ayang")
        Jumlah = int(input('jumlah minyak: '))
        if Jumlah > 21:
            print("persediaan minyak tidak sebanyak itu")
        else:
            print("minyak tersedia")
            
        main_lagi = input('kembali ke menu utama? [y/n]: ')
        if main_lagi == "y":
            Sesi4.Menu()
if __name__ == "__main__":
    shop()