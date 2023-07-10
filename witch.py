from Person import Person
from Fibonacci import Fibonacci

# function untuk mendapatkan rata-rata
def average(a, b):
    return ((a + b) / 2)

# main function for the witch
# AOD = Age of Death
# YOD = Year of Death
def mainProgram(nameA, AODA, YODA, nameB, AODB, YODB):
    # deklarasi objects Person
    personA = Person(nameA, AODA, YODA)
    personB = Person(nameB, AODB, YODB)

    personA.showPerson()
    tahunA = personA.YOD - personA.AOD
    if tahunA <= 0:
        print("-1")
    else:
        resultA = 0
        for i in range(1,tahunA+1):
            resultA = Fibonacci(i)
        print(resultA)

    personB.showPerson()
    tahunB = personB.YOD - personB.AOD
    if tahunB <= 0:
        print("-1")
    else:
        resultB = 0
        for i in range(1,tahunB+1):
            resultB = Fibonacci(i)
        print(resultB)

    if tahunA <= 0 or tahunB <= 0:
        # Jika input user menghasilkan nilai negatif, maka dikembalikan nilai -1
        print("-1 ")
        return -1
    else:
        print("So the average is (", resultA ,'+', resultB ,")/2 = ",average((resultA), float(resultB)))
        
    return average((resultA), float(resultB))

# menjalankan fungsi utama
mainProgram('A',10,12,'B',13,17)
mainProgram('A',10,12,'B',13,12)