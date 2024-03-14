#SESI 4 ADALAH "MAIN" UNTUK VASAGAME DAN VASHOP

from Function import WelcomeMessage, keluar_program
from Games import VasaGame
from Tools import Vashop

def Menu():
    user_options = int(input(f"silahkan pilih menu programnya:\n1. VasaGames\n2. Vashop\n3. Keluar\n\nSilahkan Pilih: "))
    if user_options == 1:
        VasaGame.game()
    elif user_options == 2:
        Vashop.shop()
    elif user_options == 3:
        keluar_program()
    else:
        print("pilihj yang tersedia di menu")
        
def main():
    WelcomeMessage ()
    Menu()
    
if __name__ == '__main__':
    main()
