#SOAL 1 
def fungsi_bintang() :
    while True : #infinite looping hingga input yang dimasukkan benar
        teks = input('Masukkan Sebuah Kalimat : ')
        if len(teks) > 200 : 
            print('Batas Karakter Maksimal Hanya 200')
        elif len(teks) == 0 :
            print('Masukkan Sebuah Inputan')
        else :
            output = teks.replace(' ', '').upper()
            print('*'+output+'*')
            break
