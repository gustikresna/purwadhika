#SOAL 2 - MENGURAI DAN MERAJUT KATA

def urai(word):
    output = '' #initiate string output
    for i in range(1,len(word)+1):
        output += word[0:i] #concatenate untuk setiap huruf(sesuai range iterasi ke-i)
    print(output)

urai('Codes')
urai('Python')
urai('Purwadhika')

def rajut(concatenation):
    length_spelling = 0 #initiate variable
    for i in range(1,len(concatenation)+1): #iterasi untuk mengetahui jumlah huruf
        length_spelling += i
        if length_spelling == len(concatenation): #jika total huruf yg dijumlahkan sama dengan panjang huruf,
            length_word = i #panjang kata sebenarnya merupakan "i" yang terakhir
            break
    
    print(concatenation[-length_word:]) #print kata sebenarnya

rajut('CCoCodCodeCodes')
rajut('PPyPytPythPythoPython')
rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika')
