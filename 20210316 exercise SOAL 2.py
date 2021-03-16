#SOAL 2
def input_no_hp():
    while True: #infinite looping hingga input yang dimasukkan benar
        no_hp = input('Masukkan Nomor HP : ')

        if len(no_hp) > 13: #jika no. hp diatas 13 digit
            print('Nomor HP hanya maksimal 13 Angka')
        elif no_hp[:2] != '08' : #jika tidak diawali 08
            print('Nomor HP harus dimulai dengan "08"')
        else :
            print('Nomor HP Saya adalah', no_hp)
            break