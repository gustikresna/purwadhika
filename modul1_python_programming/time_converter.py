#SOAL 2 - KONVERSI WAKTU
def time_converter(seconds) :
    if seconds.isdecimal() and int(seconds) < 359999: #jika inputan hanya digit dan dibawah 359999 detik
        HH = int(seconds) // 3600 #menghitung jam
        MM = int(seconds) % 3600 // 60 #menghitung menit
        SS = int(seconds) % 3600 % 60 #menghitung detik
        print('{:02d}:{:02d}:{:02d}'.format(HH,MM,SS))#print format digit 2  
    else :
        print('Invalid Input!') #jika input tidak sesuai

detik = input('Masukkan detik : ')
time_converter(detik)
