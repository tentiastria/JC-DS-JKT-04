
#Soal 1
# angka = int(input('Masukkan angka: '))

# if (angka%2 == 0 ):
#     print('Angka {} tergolong bilangan GENAP!'.format(angka))
# else:
#     print('Angka {} tergolong bilangan GANJIL!'.format(angka))    


# #Soal 2
# massa = float(input('Masukkan Massa(kg): '))
# tinggi = float(input('Masukkan Tinggi(cm): '))
# tinggi_m = tinggi/100
# imt = massa/(tinggi_m**2)

# if imt < 18.5:
#     k= 'BERAT BADAN KURANG!'
# elif (imt >= 18.5 and imt <= 24.9):
#     k= 'BERAT BADAN IDEAL!'
# elif (imt >= 25.0 and imt <= 29.9):
#     k= 'BB BERLEBIH!'
# elif (imt >= 30.0 and imt <= 39.9):
#     k= 'BB SANGAT BERLEBIH!'
# else: 
#     k= 'OBESITAS'

# print ('Massa {} kg & tinggi {} m'.format(massa, tinggi_m))
# print ('IMT = ' + str(imt) + ', '+ k)






nilai = 50

if nilai <60 :
    if nilai <50 :
        print('Ok')
    else:
        print('Good')
elif nilai > 100:
    print('No')
else:
    print('Great')    
