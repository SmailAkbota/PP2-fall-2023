def histogram(lst):
    for i in lst:
        for j in range(i):
            print('*', end='')
        print()

histogram([1, 3, 3, 9, 5])