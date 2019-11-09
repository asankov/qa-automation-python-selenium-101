IS_TRUE = True
IS_FALSE = False

FIBONACCI_NUMBERS = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


def num_add(a, b):
    return a + b


def num_sub(a, b):
    return a - b


def num_mul(a, b):
    return a * b


def num_div(a, b):
    return a / b


def num_floor(a, b):
    return a // b


def num_rem(a, b):
    return a % b


PANCAKE_INGREDIENTS = {
    'flour': 2,
    'eggs': 4,
    'milk': 200,
    'butter': False,
    'salt': 0.001,
}


def ingredient_exists(ingr, dict):
    return ingr in dict


def fatten_pancakes(dict):
    new_dict = dict.copy()
    new_dict['eggs'] = 6
    new_dict['butter'] = True
    return new_dict


def add_sugar(dict):
    new_dict = dict.copy()
    new_dict['sugar'] = True
    return new_dict


def remove_salt(dict):
    new_dict = dict.copy()
    del new_dict['salt']
    return new_dict


def add_fibonacci(lst):
    lst.append(lst[-1] + lst[-2])
    return lst


def fib_exists(lst, n):
    return lst.count(n) > 0


def which_fib(lst, n):
    return lst.index(n) + 1
