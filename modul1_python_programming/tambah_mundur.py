#SOAL TAMBAH MUNDUR
def tambahMundur(x,y):

    if x.isnumeric() and y.isnumeric() and int(x) <= 359999 and int(y) <=359999: #cek untuk memastikan input numeric dan dibawah sama dengan 359999
        #1. balikkan angka input
        reverse_1 = '' #initiate string untuk input 1 yg dibalik
        for i in range(len(x),0,-1): #looping untuk setiap digit input 1 dari belakang
            reverse_1 += x[i-1] #membentuk string input 1 yg dibalik

        reverse_2 = '' #initiate string untuk input 2 yg dibalik
        for i in range(len(y),0,-1): #looping untuk setiap digit angka 2 dari belakang
            reverse_2 += y[i-1] #membentuk string angka 2 yg dibalik

        #2. hitung hasil tambah
        result = int(reverse_1) + int(reverse_2) #hitung hasil tambah
        result = str(result) #convert ke string untuk memudahkan pembalikan
        
        #3. balikkan hasil tambah
        result_reverse = '' #initiate string untuk pembalikan hasil
        for i in range(len(result),0,-1): #looping untuk setiap digit hasil dari belakang
            result_reverse += result[i-1] #membentuk string digit hasil yg dibalik
        result_reverse = int(result_reverse) 

        print('Hasil tambah mundurnya : ', result_reverse) #print result

    else: #jika tidak memenuhi kriteria
        None


#looping input angka untuk pengecekan kriteria input satu per satu
#jika tidak memenuhi, stop input
while True:
    x='' #initiate x, sehingga meskipun input d break, nilai x tetap ada dan function tetap dapat dijalankan
    y='' #initiate y, sehingga meskipun input d break, nilai y tetap ada dan function tetap dapat dijalankan
    x = input('Masukkan angka 1 : ')
    if not x.isnumeric() or int(x) > 359999: #cek jika tidak numeric dan jika lebih dari 359999
        print('Invalid Input!')
        break

    y = input('Masukkan angka 2 : ')
    if not y.isnumeric() or int(y) > 359999 : #cek jika tidak numeric dan jika lebih dari 359999
        print('Invalid Input!')
        break

    if x != '' and y != '' : #jika x dan y sudah terisi
        break

tambahMundur(x,y)
