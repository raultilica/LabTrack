def insertion_sort(lista, key = lambda x: x, cmp = lambda x, y: x > y, reverse = False):
    """
    Functia sorteaza o lista prin insertion sort, in functie de mai multi parametrii, setati initial la parametrii necesari sortarii crescatoare a unei liste de tipuri de date simple
    :param lista: lista
    :param key: returneaza elementul de comparat
    :param cmp: functie de comparare, returneaza True daca expresia transmisa este adevarata, False in caz contrar
    :param reverse: functie booleana, False - sirul va fi sortat in ordinea tranmisa functiei de comparatie cmp, pentru True va inversa lista dupa comparare
    :return: o lista sortata
    """
    for index in range(1, len(lista)):
        curr = lista[index]
        prev = index - 1
        while prev >= 0 and cmp(key(lista[prev]), key(curr)):
            lista[prev + 1] = lista[prev]
            prev -= 1
        lista[prev + 1] = curr
    if reverse:
        lista.reverse()
    return lista

def comb_sort(lista, key = lambda x: x, cmp = lambda x, y: x > y, reverse = False):
    """
    Functia sorteaza o lista prin comb sort, in functie de mai multi parametrii, setati initial la parametrii necesari sortarii crescatoare a unei liste de tipuri de date simple
    :param lista: lista
    :param key: returneaza elementul de comparat
    :param cmp: functie de comparare, returneaza True daca expresia transmisa este adevarata, False in caz contrar
    :param reverse: functie booleana, False - sirul va fi sortat in ordinea tranmisa functiei de comparatie cmp, pentru True va inversa lista dupa comparare
    :return: o lista sortata
    """
    gap = len(lista)
    shrink = 1.3
    sortat = False
    while not sortat or gap > 1:
        sortat = True
        gap = max(1, int(gap / shrink))
        i = 0
        while i + gap < len(lista):
            if cmp(key(lista[i]), key(lista[i + gap])):
                lista[i], lista[i + gap] = lista[i + gap], lista[i]
                sortat = False
            i += 1
    if reverse:
        lista.reverse()
    return lista


