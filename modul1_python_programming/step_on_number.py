#SOAL STEP ON NUMBER
def steponNumber(list_number):
    list_output = []
    #cek criteria
    for i in list_number:
        x = i[0] #koordinat x
        y = i[1] #koordinat y

        #jika x atau y negatif
        if x < 0 or y < 0 : 
            output = 'No Number' 
            list_output.append(output) #tambahkan ke list output (list output di bawah di skip karena menggunakan continue)
            continue #skip ke next loop

        # kriteria garis diagonal (x dan y sama) dan (x - y = 2)
        elif x - y == 0 or x - y == 2:
            if x == 0: # jika x & y = 0, output 0
                output = 0
            elif x == 1: # jika x & y = 1, output 1
                output = 1
            elif x % 2 == 0: # jika x & y genap, output x+y
                output = x + y
            else : # jika x & y ganjil, output (x+y)-1
                output = (x + y) - 1

        else : #jika bukan koordinat garis diagonal di soal
            output = 'No Number'
        
        list_output.append(output)
    
    return list_output

list_awal = [[4,2], [6,6], [3,4]]
print(steponNumber(list_awal))
