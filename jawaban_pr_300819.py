# #Duplikat Map
# def maplist(function,list_container):
#     hasil =[]
#     for item in list_container:
#         hasil.append(function(item))
#     return hasil

list_kata=['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari Ayam']

# print(maplist(lambda x: x.lower(), list_kata))

# #Duplikat Fiter
# def filterlist(function,list_container):
#     hasil = []
#     for i in list_container:
#         if function(i):
#             hasil.append(i)
#     return hasil

# print(filterlist(lambda x: 'K' in x, list_kata))

#Fungsi Filter List
# def fillist(x):
#     for idx, word in enumerate(x):
#         lowword = word.lower()
#         x[idx] = lowword
#     search = input('Masukkan kata kunci: ').lower()
#     b = (list(filter(lambda a: search in a, x)))
#     for idx, word in enumerate(b):
#         capword = word.capitalize()
#         b[idx] = capword
#     return print(b)    

# fillist(list_kata)

#Fungsi Jumlah Kata
# def jumlah_kata(string):
#     kata = {}
#     for word in string.lower().split():
#         if word in kata.keys():
#             kata[word] += 1
#         else:
#             kata[word] = 1
#     for keys, val in kata.items():
#         print("Jumlah kata '{}' ada sebanyak {}".format(keys.capitalize(), val))        

# kata = 'Aku baru makan nasi terus aku mau makan mie nanti malam'        
# jumlah_kata(kata)



# ## Soal Bonus
import random

# Generate_x*y_angka
def number_generate(x):
    number = []
    pilihan = int(input('Pilih\n1.Angka urut\n2.Angka random\nMasukkan pilihan: '))
    if pilihan == 1:
        for i in range(x):
            temp_number =[]
            for j in range(x):
                temp_number.append((j+1)+(i*x))
            number.append(temp_number)
    elif pilihan == 2:            
        for i in range(x):
            temp_number = []
            for j in range(x):
                temp_number.append(random.randint(1,101))
            number.append(temp_number)   
    return number

# # Print_angka
def print_angka(angka):
    for i in angka:
        z = ''
        for j in (range(len(angka))):
            z += str(i[j])
            z += ' '
        print(z)

# #Memutar
def putarputar():
    ukuran = int(input('Masukkan ukuran: '))
    angka = number_generate(ukuran)
    print_angka(angka)
    putar = input('Putar ke arah?: ')
    kali = int(input('Putar berapa kali: '))
    if putar == 'Kanan' or putar == 'kanan':
        for c in range(kali):
            list_kanan = []
            for i in range(len(angka)):
                list_temp =[]
                for j in range((len(angka)-1),-1,-1):
                    list_temp.append(angka[j][i])
                list_kanan.append(list_temp)
            angka = list_kanan            
    elif putar == 'Kiri' or putar == 'kiri':
        for c in range(kali):
            list_kiri = []
            for i in range((len(angka)-1),-1,-1):
                list_temp =[]
                for j in range((len(angka))):
                    list_temp.append(angka[j][i])
                list_kiri.append(list_temp)    
            angka = list_kiri
    print_angka(angka)
                
while(True):
    angka = []
    putarputar()
    exit = input('Coba lagi [y/n]: ')
    if exit == 'y':
        True
    elif exit == 'n':
        print('Terima kasih')
        break    
