def sum_recursivly(numb):
    if numb == 0:
        return 1
    return numb * sum_recursivly(numb - 1)

print(sum_recursivly(10))