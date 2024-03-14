import socket
from time import sleep
PC_NAME = socket.gethostname()

def WelcomeMessage():
    style = "=" * (len(PC_NAME) + 6)

    print(style)
    print(f"== {PC_NAME} ==")
    print(style)
    
def keluar_program():
    print('program akan dihentikan')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Program dihentikan')

if __name__ == '__main__':
    WelcomeMessage()
    keluar_program()