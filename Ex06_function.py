#  *은 가변인수이다
def add_many(*args):
    t = 0
    for n in args:
        t += sum(n)
    return t


add_many(1, 2, 3)
add_many(1, 2, 3, 4, 5, 6)
add_many((1, 2, 3, 4, 5, 6), (1, 2), [1, 2, 3])
add_many([1, 2, 3, 4, 5, 6])
