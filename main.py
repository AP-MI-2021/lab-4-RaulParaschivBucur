
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

def intersectie_liste(lst1, lst2):
    """
    Gaseste lista care reprezinta intersectia a doua liste initiale
    :param lst1: lista 1
    :param lst2: lista 2
    :return: o lista reprezentand intersectia celor doua liste
    """
    result_lst = []
    if len(lst1) <= len(lst2):
        for elem in lst1:
            if (elem in lst2) and (elem not in result_lst):
                result_lst.append(elem)
    else:
        if len(lst1) > len(lst2):
            for elem in lst2:
                if (elem in lst1) and (elem not in result_lst):
                    result_lst.append(elem)
    return result_lst


def test_intersectie_liste():
    assert intersectie_liste([12, 22, 36, 424], [22, 23, 36, 55, 424]) == [22, 36, 424]
    assert intersectie_liste([], []) == []


# 4

def lista_cu_concatenari(lst1, lst2):
    """
    Formeaza o lista cu concatenarile elementelor din listele lst1 si lst2
    """
    result_lst = []
    if len(lst1) >= len(lst2):
        for idx in range(0, len(lst2)):
            result_lst.append(str(lst1[idx]) + str(lst2[idx]))
    elif len(lst1) < len(lst2):
        for idx in range(0, len(lst1)):
            result_lst.append(str(lst1[idx]) + str(lst2[idx]))
    return result_lst


def test_lista_cu_concatenari():
    assert lista_cu_concatenari([12, 22, 36, 11], [21, 23, 63, 55, 424]) == ['1221', '2223', '3663', '1155']


def este_palindrom(s):
    """
    Verifica daca un sir este palindrom
    """
    return s == s[::-1]


def test_este_palindrom():
    assert este_palindrom('121') is True
    assert este_palindrom('1212') is False



def af_palindroame(lst):
    """
    Returneaza lista formata din palindroamele prezente in lista lst
    """
    result_lst = []
    for elem in lst:
        if este_palindrom(elem):
            result_lst.append(int(elem))
    return result_lst


def test_af_palindroame():
    assert af_palindroame(['121', '22322', '112']) == [121, 22322]
    assert af_palindroame([]) == []


def main():
    lst1 = []
    lst2 = []
    while True:
        print(' ')
        print('1. Citire lista1 si lista 2')
        print('2. Af daca cele 2 liste au acelasi nr de elemente pare')
        print('3. Af o listă reprezentând intersecția listelor citite de la tastatură')
        print('4. Af toate palindroamele obținute prin concatenarea elementelor de pe aceleași poziții în'
              'cele doua liste')
        print('5. Citiți o a treia listă și afișați listele obținute prin înlocuirea în cele două liste citite la'
              ' punctul 1 a tuturor elementelor cu oglinditul lor dacă îndeplinesc următoarea regulă: elementele sunt'
              ' divizibile cu toate elementele din a treia lista. Dacă nu îndeplinesc regula, păstrați elementul așa cum e.')
        print('6. Iesi')
        optiune = int(input('Alege o optiune: '))

        if optiune == 1:
            print('Lista 1:')
            lst1 = read_list()
            print('Lista 2:')
            lst2 = read_list()

        elif optiune == 2:
            if cate_nr_pare(lst1) == cate_nr_pare(lst2):
                print('Au acelasi nr de elem pare')
            else:
                print('NU au acelasi nr de elemente pare')

        elif optiune == 3:
            print('Intersectia celor doua liste este: ', intersectie_liste(lst1,lst2))

        elif optiune == 4:
            lst_concat = lista_cu_concatenari(lst1, lst2)
            print('elem palindroame din concatenare sunt', af_palindroame(lst_concat))
            pass
        elif optiune == 5:
            pass

        elif optiune == 6:
            break


test_este_palindrom()
test_lista_cu_concatenari()
test_af_palindroame()
test_intersectie_liste()
test_cate_nr_pare()
main()

