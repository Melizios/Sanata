# fungsi fibonacci
# Penjabaran penghitungan dapat dilihat dengan mengaktifkan bagian komentar di dalam fungsi
def Fibonacci(tahun):
    if tahun <=0:
        return -1
    elif tahun == 1:
        #print("On the 1st year she kills 1 villager")
        return 1
    else:
        arr = [1] * (tahun+1)
        arr[1] = 1
        hasil = arr [0] + arr[1]
        #print("On the year", tahun ,"she kills",end=' ')
        for i in range(3,tahun+1):
            arr[i] = arr[i-1] + arr[i-2]
            hasil+=arr[i]
        # for i in range(1,tahun+1):
        #     print(arr[i],end=' ')
        #     if i != tahun:
        #         print("+",end=' ')
        # print('=',hasil,"villagers")
        return hasil
 