def fun(number: int) -> bool:
    return number % 2 == 0


wynik = fun(7)
if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
