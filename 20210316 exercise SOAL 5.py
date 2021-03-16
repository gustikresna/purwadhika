#SOAL 5
def jumlah_karakter_maks() :
    text = input('Masukkan Kalimat : ')
    list_words = text.split() #

    length_words = []
    for i in list_words:
        length_words.append(len(i))
    max_word = max(length_words)
    print(length_words)
    print('Karakter yang terbanyak adalah sebesar', max_word, 'karakter')

    for i in range(len(length_words)):
        if length_words[i] == max_word:
            print('Karakter yang berjumlah', max_word, 'adalah', list_words[i])
