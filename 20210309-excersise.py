#SOAL 1
def kali_lima():
    x = list(map(int,input('Masukkan Angka : ').split(' ')))
    hasil = [5 * i for i in x]
    print(hasil)

#SOAL 2
def input_data():
    n = int(input('Masukkan Banyaknya Data : '))
    x = []
    for i in range(n) :
        y = int(input('Data ke -'+str(i+1)+' = '))
        print(y)
        x.append(y)
    return x

def rata2(list_number):
    hasil = sum(list_number) / len(list_number)
    return hasil


def var_stdev(list_number,function_rata2):
    diff = []
    x_bar = rata2(list_number)
    for i in list_number:
        x = (i - x_bar)**2
        diff.append(x)
    s2 = sum(diff)/(len(list_number)-1)  
    s = s2 ** (1/2)
    print('Rata-Ratanya Adalah', rata2(list_number))
    print('Variansinya Adalah', s2)
    print('Standar Deviasinya Adalah', s)

#call function
var_stdev(input_data(), rata2)

#SOAL 3
def sorting() :
    x = list(map(int,input('Masukkan Angka').split(' ')))
    for i in range(len(x)) :
        for j in range(i+1, len(x)):
            if x[i] > x[j]:
                x[i],x[j] = x[j], x[i]
    print('Hasil sorting : ', x)
    print('Nilai terbesar dari data adalah : ', x[-1])
    print('Nilai terkeci dari data adalah : ', x[0])



#SOAL 4
def reverse_word() :
    text = input('Masukkan sebuah kalimat : ').split(' ')
    for i in range(len(text)):
        alphabet = ''
        for j in range(len(text[i]),0,-1):
            alphabet += text[i][j-1]
        print(alphabet, end=' ')

#SOAL 5
def upper_lower_case_calculator() :
    upper = 0
    lower = 0
    text = input('Masukkan Sebuah Kalimat')
    mod_text = text.replace(' ','')
    for i in mod_text:
        if i.isupper():
            upper += 1
        else:
            lower += 1
    print('Kalimat Original', text)
    print('Banyaknya jumlah huruf kapital dalam kalimat adalah : ', upper)
    print('Banyaknya jumlah huruf nonkapital dalam kalimat adalah : ', lower)



    



