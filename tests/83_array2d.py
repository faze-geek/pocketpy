from array2d import array2d

# test error args for __init__
try:
    a = array2d(0, 0)
    exit(0)
except ValueError:
    pass

# test callable constructor
a = array2d(2, 4, default=lambda: 0)

assert a.width == a.n_cols == 2
assert a.height == a.n_rows == 4
assert a.numel == 8

# test is_valid
assert a.is_valid(0, 0)
assert a.is_valid(1, 3)
assert not a.is_valid(2, 0)
assert not a.is_valid(0, 4)
assert not a.is_valid(-1, 0)
assert not a.is_valid(0, -1)

# test get
assert a.get(0, 0) == 0
assert a.get(1, 3) == 0
assert a.get(2, 0) is None
assert a.get(0, 4, default='S') == 'S'

# test __getitem__
assert a[0, 0] == 0
assert a[1, 3] == 0
try:
    a[2, 0]
    exit(1)
except IndexError:
    pass

# test __setitem__
a[0, 0] = 5
assert a[0, 0] == 5
a[1, 3] = 6
assert a[1, 3] == 6
try:
    a[0, -1] = 7
    exit(1)
except IndexError:
    pass

# test __iter__
a_list = [[5, 0], [0, 0], [0, 0], [0, 6]]
assert a_list == list(a)

# test __len__
assert len(a) == 4

# test __eq__
x = array2d(2, 4, default=0)
b = array2d(2, 4, default=0)
assert x == b

b[0, 0] = 1
assert x != b

# test __repr__
assert repr(a) == f'array2d(2, 4)'

# test map
c = a.map(lambda x: x + 1)
assert list(c) == [[6, 1], [1, 1], [1, 1], [1, 7]]
assert list(a) == [[5, 0], [0, 0], [0, 0], [0, 6]]
assert c.width == c.n_cols == 2
assert c.height == c.n_rows == 4
assert c.numel == 8

# test copy
d = c.copy()
assert d == c and d is not c

# test fill_
d.fill_(-3)
assert d == array2d(2, 4, default=-3)

# test apply_
d.apply_(lambda x: x + 3)
assert d == array2d(2, 4, default=0)

# test copy_
a.copy_(d)
assert a == d and a is not d
x = array2d(4, 4, default=0)
x.copy_(d)
assert x == d and x is not d

# test subclass array2d
class A(array2d):
    def __init__(self):
        super().__init__(2, 4, default=0)

assert A().width == 2
assert A().height == 4
assert A().numel == 8
assert A().get(0, 0, default=2) == 0

# test alive_neighbors
a = array2d(3, 3, default=0)
a.count_neighbors(0) == a
