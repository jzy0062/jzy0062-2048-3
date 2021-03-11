import hashlib
import random

myHash = hashlib.sha256()


def _create(userParms):
    grid = generate_init_grid()
    myHash.update(grid.encode())
    integrity = myHash.hexdigest().upper()
    result = {'grid': grid, 'score': 0, 'integrity': integrity, 'status': 'ok'}
    return result


def generate_init_loc():
    """
    generate 2 different place of initial two '2'.
    :return: two integer belongs to [1, 15]
    """
    loc1 = random.randint(0, 15)
    loc2 = random.randint(0, loc1-1) if loc1 > 8 else random.randint(loc1 + 1, 15)
    return loc1, loc2


def generate_init_grid():
    """
    generate initial grid string with 2 initial '2'
    :return: string of grid containing two '2' in string
    """
    loc1, loc2 = generate_init_loc()
    grid = list('0' * 16)
    grid[loc1] = '2'
    grid[loc2] = '2'
    grid2 = ""
    for i in grid:
        grid2 += i
    grid = grid2
    return grid