from math import floor
list_angka = [1,3,3,4,4,2,4 ]
# Fungsi bubblesort

def bubblesort(list):
    for k in range(len(list)-1, 0, -1):
        for i in range(k):
            if (list[i] > list[i+1]):
                list[i], list[i+1] = list[i+1], list[i]
    return list
#Fungsi Mean

# def mean_list(list):
#     z = 0
#     for i in list:
#         z += i
#     return print(z/len(list))

# mean_list(list_angka)
#Fungsi Median

# def median_list(list):
#     list = bubblesort(list)
#     print(list)
#     if len(list)%2 == 0:
#         return print((list[len(list)/2] + list[(len(list)/2)+1])/2)
#     else:
#         return print(list[floor(len(list)/2)])

# median_list(list_angka)

# #Fungsi Modus
def mode_list(list):
    ind = set(list)
    counter = {}
    modus = []
    for i in ind:
        z = 0
        for j in list:
            if i == j:
                z += 1
        counter[i] = z
    max_count = max(counter.values())
    for k in counter:
        if counter[k] == max_count:
            modus.append(k)
    if len(modus) == len(set(list)):
        modus = []
    return (print(modus))

mode_list(list_angka)

    


