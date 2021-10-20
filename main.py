
def read_list():
    lst = []
    lst_str = input('Scrie elementele listei separate prin spatiu: ')
    lst_str_split = lst_str.split(' ')
    for elem in lst_str_split:
        lst.append(int(elem))
    return lst


# 2

def cate_nr_pare(lst):
    """
    Afla cate nr pare sunt intr-o lista prin variabila cate
    """
    cate = 0
    for elem in lst:
        if elem % 2 == 0:
            cate += 1
    return cate


def test_cate_nr_pare():
    assert cate_nr_pare([]) == 0
    assert cate_nr_pare([1, 2, 3, 4, 4]) == 3
    assert cate_nr_pare([1, 3, 3, 7, 7]) == 0


# 3

def


def main():
    lst1 = []
    lst2 = []
    while True:
        print(' ')
        print('1. Citire lista1 si lista 2 ')
        print('2. Af daca cele 2 liste au acelasi nr de elemente pare')
        print('3.')
        print('4.')
        print('5.')
        print('6. Iesi')
        optiune = int(input('Alege o optiune: '))

        if optiune == 1:
            print('Lista 1:')
            lst1 = read_list()
            print('Lista 2:')
            lst2 = read_list()

        if optiune == 2:
            if cate_nr_pare(lst1) == cate_nr_pare(lst2):
                print('Au acelasi nr de elem pare')
            else:
                print('NU au acelasi nr de elemente pare')

        if optiune == 3:
            pass

        if optiune == 4:
            pass

        if optiune == 5:
            pass

        if optiune == 6:
            break


test_cate_nr_pare()
main()