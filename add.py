import ctypes

test_c = ctypes.CDLL('add.o')
test_c.add.argtypes = (ctypes.c_int, ctypes.c_int)

def add(x, y):
    result = test_c.add(ctypes.c_int(x), ctypes.c_int(y))
    return int(result)