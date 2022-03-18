#SOAL 4
def triangle():
    line = int(input('Masukkan Jumlah Baris : ')) #input sisi segitiga
    for i in range(line):
        if i == 0: #baris paling atas
            print((line-(i+1))*' ' + '*'*3)
        elif i == (line - 1): #baris paling bawah
            print('*' * (line*2+1))
        else :  #baris tengah
            print((line-(i+1))*' ' + '*'*2 + (i*2-1)*' ' + '*'*2)
