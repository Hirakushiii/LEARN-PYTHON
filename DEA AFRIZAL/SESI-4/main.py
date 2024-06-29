from lib import welcome_msg, exit_program
from games import tebak_goa

def menu() :
    user_opt = int(input(f'Silahkan pilih menu game yang akan dimainkan...\n1.Tebak Goa\n2.Exit Program\n: '))
    if user_opt == 1 :
        tebak_goa.play_game()
    elif user_opt == 2 :
        exit_program()
        exit()
    else :
        print('tes')


def start() :
    welcome_msg()
    menu()

if __name__ == '__main__' :
    start()