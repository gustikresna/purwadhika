#SOAL 6
def deret_ap_gp():
    while True : #infinite loop sampai 0 0 0
        x = list(map(int,input().split()))

        first_diff = x[1] - x[0] #selisih angka pertama dan kedua
        diff_list = [] #initiate list untuk menyimpan selisih tiap angka

        for i in range(len(x)-1) :
            diff = x[i+1] - x[i] #selisih tiap angka
            diff_list.append(diff) #menambahkan ke list
        
        if x == [0, 0, 0]:#break jika inputnya 0 0 0
            break
        elif sum(diff_list)/len(diff_list) == first_diff : #jika selisih rata2 sama dengan selisih pertama maka AP
            next_sqnce = x[-1] + first_diff #tambahkan deret terakhir dengan selisih
            print('AP', next_sqnce)
        else : #jika tidak maka geometri
            next_sqnce = x[-1] / x[-2] * x[-1] #deret terakhir dikali kelipatan deret
            print('GP', next_sqnce)