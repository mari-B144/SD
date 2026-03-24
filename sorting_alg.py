#bubble - O(n*n)

def bubble_sort(vector):
    n = len(vector)
    for i in range(n-1):
      ok = False
      for j in range(n-i-1):
        if vector[j] > vector[j + 1]:
          vector[j], vector[j + 1] = vector[j + 1], vector[j]
          ok = True
      if not ok:
        break
    
    return vector

#merge - O(nlogn)

def merge_sort(vector):
    if len(vector) <= 1:
        return vector

    mij = len(vector) // 2
    st = merge_sort(vector[:mij])
    dr = merge_sort(vector[mij:])

    return interclasare(st, dr)


def interclasare(st, dr):
    rezultat = []
    i = j = 0

    while i < len(st) and j < len(dr):
        if st[i] < dr[j]:
            rezultat.append(st[i])
            i += 1
        else:
            rezultat.append(dr[j])
            j += 1

    rezultat.extend(st[i:])
    rezultat.extend(dr[j:])

    return rezultat


#quick - O(nlogn)

def quick_sort(vector):
    if len(vector) <= 1:
        return vector

    pivot = vector[len(vector) // 2]
    st = []
    mij = []
    dr = []
    for x in vector:
        if x < pivot:
            st.append(x)
        elif x == pivot:
            mij.append(x)
        else:
            dr.append(x)

    return quick_sort(st) + mij + quick_sort(dr)

#heap - O(nlogn)

def heapify(vector, n, i):
    maxim = i
    st = 2 * i + 1
    dr = 2 * i + 2

    if st < n and vector[st] > vector[maxim]:
        maxim = st

    if dr < n and vector[dr] > vector[maxim]:
        maxim = dr

    if maxim != i:
        vector[i], vector[maxim] = vector[maxim], vector[i]
        heapify(vector, n, maxim)


def heap_sort(vector):
    n = len(vector)

    for i in range(n//2-1, -1, -1):
        heapify(vector, n, i)

    for i in range(n - 1, 0, -1):
        vector[i], vector[0] = vector[0], vector[i] #mut elem maxim la capatul vectorului
        heapify(vector, i, 0) #reconstruiesc heap ul pt restul elem

    return vector


#radix - O(n*k) unde k nr de cifre al nr max

def counting_sort(v, exp):
    n = len(v)
    rez = [0]*n
    frecv = [0]*10

    for i in range(n):
        index = (v[i]//exp)%10
        frecv[index] += 1 #pana la i sunt frecv[i] elem

    for i in range(1,10):
        frecv[i] += frecv[i-1]

    for i in range(n-1, -1, -1):
        index = (v[i]//exp)%10
        rez[frecv[index]-1] = v[i] #pune elem in poz coresp cifrei lui
        frecv[index] -= 1

    return rez


def radix_sort(v):
    if len(v) == 0:
        return v

    maxim = max(v)
    exp = 1
    while maxim // exp > 0:
        v = counting_sort(v, exp)
        exp *= 10

    return v

#generare vectori pt teste

import random


def generare_vector(n, minim, maxim, tip):
    v = []

    if tip == "random":
        for i in range(n):
            v.append(random.randint(minim, maxim))

    elif tip == "sortat":
        x = minim
        for i in range(n):
            v.append(x)
            x += 1

    elif tip == "invers":
        x = maxim
        for i in range(n):
            v.append(x)
            x -= 1

    elif tip == "constant":
        val = random.randint(minim, maxim)
        for i in range(n):
            v.append(val)

    elif tip == "valori_mici":
        for i in range(n):
            v.append(random.randint(0, 10))

    elif tip == "gol":
        return []

    elif tip == "un_element":
        v.append(random.randint(minim, maxim))

    return v

#masurare timp

def masurare_timp(algoritm, v):
    import time

    copie = v.copy()

    start_time = time.time()
    algoritm(copie)
    end_time = time.time()

    durata = end_time - start_time
    return durata

def raport():
    dimensiuni = [10, 100, 1000]
    tipuri = ["random", "sortat", "invers", "constant", "valori_mici", "un_element","gol"]

    algoritmi = [
        ("Bubble", bubble_sort),
        ("Merge", merge_sort),
        ("Quick", quick_sort),
        ("Heap", heap_sort),
        ("Radix", radix_sort)
    ]

    for n in dimensiuni:
        print("\nDimensiune vector:", n)

        for tip in tipuri:
            v = generare_vector(n, 0, 100000, tip)
            print("\nTip vector:", tip)

            for nume, alg in algoritmi:
                try:
                    t = masurare_timp(alg, v)
                    print(nume, "->", t)
                except:
                    print(nume, "-> eroare")


raport()