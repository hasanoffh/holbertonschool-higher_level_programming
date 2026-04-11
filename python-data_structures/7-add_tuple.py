#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Hər iki tuple üçün ilk 2 elementi təmin edirik
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # Yalnız ilk iki elementi toplayıb yeni tuple qaytarırıq
    return (a[0] + b[0], a[1] + b[1])
