import socket
from time import sleep

name = socket.gethostname()

def welcome_msg() :
    a = '*' * (len(name) + 8)
    print(a)
    print(f'*** {name} ***')
    print(a)

def exit_program() : 
    print('Program akan dihentikan dalam :')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Program berhasil dihentikan!')

if __name__ == '__main__' :
    welcome_msg()
    exit_program()