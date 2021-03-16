#SOAL 5
def jumlah_karakter_maks() :
    text = input('Masukkan Kalimat : ')
    list_words = text.split() #split spasi

    length_words = [] #initiate list untuk jumlah karakter tiap huruf
    for i in list_words: #looping untuk seluruh kata dalam kalimat
        length_words.append(len(i)) #menghitung panjang karakter dan memasukkan ke dalam list
    max_word = max(length_words) #mengambil nilai jumlah maksimum huruf
    print(length_words)
    print('Karakter yang terbanyak adalah sebesar', max_word, 'karakter')

    for i in range(len(length_words)): #looping untuk print kata sesuai index maksimum length_words
        if length_words[i] == max_word:
            print('Karakter yang berjumlah', max_word, 'adalah', list_words[i])
