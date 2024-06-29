import random

message = 'WELCOME TO GAME TEBAK TIKUS'
lubang_tikus = random.randint(1,4)

print('***********************************')
print(f'*** {message} ***')
print('***********************************')

nama = input('Tuliskan namamu disini: ')
print(f'Halo {nama}! Coba Perhatikan Lubang Dibawah Ini\n|_|     |_|     |_|     |_|')

pilihan_user = int(input('Menurut kamu dimanakan tikus itu berada?... [1 / 2 / 3 / 4] : '))
yakin = input(f'Apakah kamu sudah yakin dengan jawabanmu yaitu {pilihan_user}? [y/n] : ')

if yakin == 'n' :
    print('Silahkan Ulang Kembali Program!')
    exit()
elif yakin == 'y' :
    if pilihan_user == lubang_tikus:
        print(f'KAMU MENANG! Tikus itu berada pada lubang {lubang_tikus}, Dan kamu memilih lubang {pilihan_user}')
    else :
        print(f'Kamu Kalah! Tikus itu berada pada lubang {lubang_tikus}, Dan kamu memilih lubang {pilihan_user}')
else :
    print('Kamu Memasukkan Input Tidak Sesuai Pilihan. Silahkan Ulangi Programnya!')
    exit()