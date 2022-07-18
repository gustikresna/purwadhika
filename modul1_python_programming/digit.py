#SOAL DIGIT
def digitAwal(a,b):
    result = a ** b #hitung result = a pangkat b
    result_string = str(result) #convert result ke string untuk memudahkan pengambilan digit
    return int(result_string[0]) #ambil digit awal

def digitAkhir(a,b):
    result = a ** b #hitung result = a pangkat b
    result_string = str(result) #convert result ke string untuk memudahkan pengambilan digit
    return int(result_string[-1]) #ambil digit akhir

print(digitAwal(10,8))
print(digitAwal(2,3))
print(digitAwal(6,3))

print(digitAkhir(10,8))
print(digitAkhir(2,3))
print(digitAkhir(6,3))
