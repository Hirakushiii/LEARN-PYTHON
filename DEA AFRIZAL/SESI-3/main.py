import random
from lib import welcome_msg

message = 'WELCOME TO GAME TEBAK TIKUS V1 BY-KENN'
lubang_tikus = random.randint(1,4)

welcome_msg(message)

nama = input('Tuliskan namamu disini: ')
while nama == '':
    nama = input('Tuliskan namamu dulu bro :')

goa = '  |_|  '
goa_kosong = [goa] * 4
goaBerIsi = goa_kosong.copy()
goaBerIsi[lubang_tikus - 1] = '|0_0|'

# print(all_goa)

goa_kosong = '   '.join(goa_kosong)
goaBerIsi = '   '.join(goaBerIsi)

while True :
    lubang_tikus = random.randint(1,4)
    goa_kosong = [goa] * 4
    goaBerIsi = goa_kosong.copy()
    goaBerIsi[lubang_tikus - 1] = '|0_0|'

    goa_kosong = '   '.join(goa_kosong)
    goaBerIsi = '   '.join(goaBerIsi)

    print(f'''Halo {nama}! Coba Perhatikan Lubang Dibawah Ini\n
    {goa_kosong}
    ''')

    pilihan_user = int(input('Menurut kamu dimanakan tikus itu berada?... [1 / 2 / 3 / 4] : '))
    while pilihan_user > 4 :
        pilihan_user = int(input('Input Harus salah satu dari angka 1 / 2 / 3 / 4 : '))
    yakin = input(f'Apakah kamu sudah yakin dengan jawabanmu yaitu {pilihan_user}? [y/n] : ')

    if yakin == 'n' :
        print('Silahkan Ulang Kembali Program!')
        exit()
    elif yakin == 'y' :
        if pilihan_user == lubang_tikus:
            print(f'\n{goaBerIsi} \n\nKAMU MENANG! Tikus Itu Berada Pada Kubang {lubang_tikus}, Dan Kamu Memilih Lubang {pilihan_user}')
        else :
            print(f'\n{goaBerIsi} \n\nKamu Kalah! Tikus Itu Berada Pada Lubang {lubang_tikus}, Dan Kamu Memilih Lubang {pilihan_user}')
    else :
        print('Kamu Memasukkan Input Tidak Sesuai Pilihan. Silahkan Ulangi Programnya!')
        exit()

    playagain = input('\n\nMasih ingin bermain? [y/n]')
    if playagain == 'n' :
        break

print('Program Selesai!')