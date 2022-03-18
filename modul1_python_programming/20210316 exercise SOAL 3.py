#SOAL 3
x = [1, 3, 2, 2, 1, 5, 1, 24, 12, 124, 12, 21, 32, 15]
def sort_odd_even(x) :
    odd = [] #initiate empty list untuk bilangan ganjil
    even = [] #initiate empty list untuk bilangan genap
    for i in x :
        if i % 2 == 0: #jika genap
            even.append(i)
        else : #ganjil
            odd.append(i)

    even.sort(reverse=True) #sort descending untuk bilangan genap
    odd.sort() #sort ascending untuk bilangan ganjil
    sorted_list = odd+even #gabungkan list
    return sorted_list
