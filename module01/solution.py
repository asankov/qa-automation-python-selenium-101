def f_c(x):
    '''
    returns 4 for every input parameter
    '''
    return 4


def f_x(x, a, b):
    return a * x + b


def sum(x):
    return f_x(x, 1, 1) + f_x(x, 2, 2) + f_x(x, 3, 3)
