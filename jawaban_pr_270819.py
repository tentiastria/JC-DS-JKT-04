# 1. Given a four-digit number, perform its cyclic rotation by two digits

# a = int(input('Masukkan Angka:'))
# print(a % 100 * 100 + a // 100)


# 2. Given a radius of the circle, calculate the area of the circle

# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# 3. Given two two-digit numbers, merge their digits as shown in the tests below.

# a = int(input('Masukkan 2 angka pertama: '))
# b = int(input('Masukkan 2 angka kedua: '))
# tens_a = a // 10
# units_a = a % 10
# tens_b = b // 10
# units_b = b % 10
# print(tens_a * 1000 + tens_b * 100 + units_a * 10 + units_b)


# 4. Given a string. Create a program to remove the character you want

# a = input('Masukkan Kata: ')
# rep = input('Kata yang dihilangkan: ')
# rep2 = input('Kata yang dihilangkan: ')
# hilang =  a.replace(rep, '')
# print(hilang.replace(rep2, ''))


# 5. Given a string consisting of exactly two words separated by a space. 
# Print a new string with the first and second word positions swapped (the second word is printed first).

a = input('Masukkan Kata: ')
lis = a.split()
print(lis)
print(lis[1] +' '+ lis[0])