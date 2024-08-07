import ctypes
clib = ctypes.CDLL("/home/rohit/Desktop/Day5/Ctypes2/dir_2/first.so")

clib.printMessage.argtypes = []
clib.printMessage.restype = None

clib.printSum.argtypes = [ctypes.c_int, ctypes.c_int]
clib.printSum.restype = None

clib.printString.argtypes = [ctypes.c_char_p]
clib.printString.restype = None

clib.printMessage()
clib.printSum(6,8)
clib.printString("Hello from Python")
