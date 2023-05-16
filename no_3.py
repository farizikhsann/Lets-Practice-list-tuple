l1 = [2, 4, 3]
l2 = [5, 6, 4]
hasil = []

def add(list1, list2):
    list1.reverse()
    list2.reverse()
    sisa = 0
    for i in range(len(list1)):
        tambah = list1[i] + list2[i]

        if(len(str(tambah)) == 1):
            hasil.insert(i,tambah+sisa)

        elif((len(str(tambah)) > 1)):
            hasil.insert(i,tambah- (10**(len(str(tambah))-1)))
            sisa += (len(str(tambah))-1)
if __name__ == '__main__':

    add(l1, l2)
    print(hasil)
