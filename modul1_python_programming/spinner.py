#SOAL 1 - LIST SPINNER #hanya berfungsi untuk matrix persegi
list_awal = [[1,2,3],
            [4,5,6],
            [7,8,9]]

def counterClockwise(list_awal):
    list_result = [ [] for a in range(len(list_awal))] #initiate list inside list output
    for i in range(len(list_awal)): #looping untuk setiap outside list
        for j in range(len(list_awal[i])-1,-1,-1): #looping untuk setiap inside list (reverse)
            list_result[j].append(list_awal[i][len(list_awal[i])-1-j]) #add data ke list result

    print(*list_result,sep='\n')

counterClockwise(list_awal)
