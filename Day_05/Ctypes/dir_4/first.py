import ctypes
clib = ctypes.CDLL("/home/rohit/Desktop/Day5/Ctypes/dir_4/first.so")
clib.display1()
clib.display2(7,8)
