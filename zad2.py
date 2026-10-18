def fun_a(name_list: list):
    for element in name_list:
        print(element+'\n')


def fun_bv1(number_list: list):
    newlist = []
    for element in number_list:
        newlist.append(element << 1)
    return newlist


def fun_bv2(number_list: list):
    return [number << 1 for number in number_list]


def fun_c(number_list: list):
    for n in range(0, len(number_list)):
        if number_list[n] % 2 == 0:
            print(number_list[n])


def fun_d(number_list: list):
    for n in range(0, len(number_list), 2):
        print(number_list[n])


if __name__ == '__main__':
    fun_a(["maciek", "maciek1", "maciek2", "maciek3", "maciek4"])
    print(fun_bv1([1, 2, 3, 4, 5]))
    print(fun_bv2([1, 2, 3, 4, 5]))
    fun_c([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    fun_d([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
