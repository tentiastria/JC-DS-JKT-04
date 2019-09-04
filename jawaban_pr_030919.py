# Jawaban highest sequence num
# def get_highest_xnum(num, sequence):
#    from math import floor,pow

#    if num < pow(10,sequence) or sequence >5:
#       print('Input valid num or sequence')
#    else:
#       angka = []
#       while (num > 0):
#          angka.append(num%10)   
#          num = floor(num/10)
#       highest = 0
#       for idx in range(len(angka)-1,sequence-2,-1):
#          test = ''
#          for i in range(sequence):
#             test += str(angka[idx-i])   
#          if int(test) > highest:
#             highest = int(test)
#       print('The highest {}-number is {}'.format(sequence,highest))
      
# get_highest_xnum(87191973114, 4)






#Jawaban Pesan Tiket

film = {1:'The Incredibles', 2:'Toy Story'}
jadwal = {1: 'Siang', 2: 'Malam'}
kursi_history = {}

for i in film.values():
    for j in jadwal.values():
        kursi_history[i+j] = 0
history = {}

def kursi():
    c = []
    for i in range(2):
        d = []
        for j in range(10):
             d.append('O') 
        c.append(d)
    return c          

def pesan_tiket():
    print('List film:\n1. The Incredibles\n2. Toy Story')
    while(True):
        pilih_film = int(input('Silakan Pilih Film: '))
        if pilih_film == 1 or pilih_film == 2:
            break
    while(True):
        pilih_jadwal= int(input('Pilih Jadwal film {}:\n1. Siang\n2. Malam\nPilihan:'.format(film[pilih_film])))
        if pilih_jadwal == 1 or pilih_jadwal == 2:
            break
    while(True):
        tiket_kali = int(input('Pesan Tiket Berapa kali: '))
        if tiket_kali > 0 or tiket_kali <= 20:
            break      
    def pesan_kursi(kali):
        for i in range(kali):
            row = int(input('Row:'))
            seat = int(input('Seat:'))
            if kursi_history[film[pilih_film]+jadwal[pilih_jadwal]][row-1][seat-1] == 'O':
                kursi_history[film[pilih_film]+jadwal[pilih_jadwal]][row-1][seat-1] = 'X'                
            else:
                print('Kursi Tidak Tersedia')   
            j = ''
            for k in range(2):
                for l in kursi_history[film[pilih_film]+jadwal[pilih_jadwal]][k]:
                    j += l
                j += '\n'         
            history[film[pilih_film]+jadwal[pilih_jadwal]+str(row)+str(seat)] = [film[pilih_film],jadwal[pilih_jadwal],row,seat]      
            print('Tempat Duduk\n'+j)                      
    if kursi_history[film[pilih_film]+jadwal[pilih_jadwal]] == 0:
        kursi_history[film[pilih_film]+jadwal[pilih_jadwal]] = kursi()
        pesan_kursi(tiket_kali)
    else:
        pesan_kursi(tiket_kali)   

                      
def lihat_history():
    for i in history.values():
        print('Film {two} Jadwal {kucing} Seat {three} Row {four}'.format(kucing = i[0], two=i[1], three=i[2], four=i[3]))
        
while(True):
    pilih = int(input('Menu:\n1. Pesan Tiket\n2. Lihat History\n3. Keluar\nTentukan pilihan:'))
    if pilih == 1:
        pesan_tiket()
    elif pilih == 2:
        lihat_history()
    elif pilih == 3:
        break            

