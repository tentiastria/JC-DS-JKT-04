import random

def menu():
    while(True):
        print('\nApp Ramalan Terkini\n')
       
        print('Pilih Ramalan anda: \n1. Ramalan Pekerjaan \n2. Ramalan Kesehatan \n3. Ramalan Percintaan \n4. Keluar')
        pilih = int(input('Masukkan Pilihan: '))
        if pilih < 1 or pilih >4:
            print('Invalid Input')
        elif pilih == 1:
            uang = int(input('\nMasukkan Sumbangan uang (Rupiah): '))
            ramal_kerja(uang)
        elif pilih == 2:
            uang = int(input('\nMasukkan Sumbangan uang (Rupiah): '))
            ramal_kesehatan(uang)
        elif pilih == 3:
            uang = int(input('\nMasukkan Sumbangan uang (Rupiah): '))
            ramal_cinta(uang)
        else:
            print('Terima Kasih')
            break            

def ramal_kerja(uang):
    kerja = {1:'Kerjaan anda akan Lancar', 2:'Tidak ada perubahan berarti', 
        3:'perlu istirahat yang cukup', 4:'Akan lebih baik kedepannya', 5:'Pekerjaan akan terhambat'}
    peluang = []
    if uang < 10000:
        for i in range(8):
            peluang.append(random.randint(3,5))
        for i in range(1,3):
            peluang.append(i)
        print('\nHasil Ramalan: {}'.format(kerja[peluang[random.randint(0,9)]]))
    elif uang > 10000 and uang <50000 :
        for i in range(8):
            peluang.append(random.randint(2,4))
        peluang.append(1)
        peluang.append(5)
        print('\nHasil Ramalan: {}'.format(kerja[peluang[random.randint(0,9)]]))            
    else:
        for i in range(8):
            peluang.append(random.randint(1,3))
        for i in range(4,6):
            peluang.append(i)
        print('\nHasil Ramalan: {}'.format(kerja[peluang[random.randint(0,9)]])) 
                
def ramal_kesehatan(uang):
    sehat = {1:'Kesehatan akan baik-baik saja', 2:'Tidak ada masalah kesehatan', 
        3:'Banyak minum air', 4:'Kesehatan memburuk', 5:'Kemungkinan sakit besar'}
    peluang = []
    if uang < 10000:
        for i in range(8):
            peluang.append(random.randint(3,5))
        for i in range(1,3):
            peluang.append(i)
        print('\nHasil Ramalan: {}'.format(sehat[peluang[random.randint(0,9)]]))
    elif uang > 10000 and uang <50000 :
        for i in range(8):
            peluang.append(random.randint(2,4))
        peluang.append(1)
        peluang.append(5)
        print('\nHasil Ramalan: {}'.format(sehat[peluang[random.randint(0,9)]]))            
    else:
        for i in range(8):
            peluang.append(random.randint(1,3))
        for i in range(4,6):
            peluang.append(i)
        print('\nHasil Ramalan: {}'.format(sehat[peluang[random.randint(0,9)]])) 
 
def ramal_cinta(uang):
    cinta = {1:'Hubungan akan berjalan baik', 2:'Akan bertemu dia yang ditunggu', 
        3:'Sering-sering mencari kenalan baru', 4:'Tidak ada perubahan berarti dengan kondisi sekarang', 5:'Sebaiknya mundur saja'}
    peluang = []
    if uang < 10000:
        for i in range(8):
            peluang.append(random.randint(3,5))
        for i in range(1,3):
            peluang.append(i)  
        print('\nHasil Ramalan: {}'.format(cinta[peluang[random.randint(0,9)]]))
    elif uang > 10000 and uang <50000 :
        for i in range(8):
            peluang.append(random.randint(2,4))
        peluang.append(1)
        peluang.append(5)
        print('\nHasil Ramalan: {}'.format(cinta[peluang[random.randint(0,9)]]))          
    else:
        for i in range(8):
            peluang.append(random.randint(1,3))
        for i in range(4,6):
            peluang.append(i)
        print('\nHasil Ramalan: {}'.format(cinta[peluang[random.randint(0,9)]]))

menu()                                  