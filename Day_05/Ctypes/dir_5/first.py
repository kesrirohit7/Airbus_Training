import ctypes
clib = ctypes.CDLL("/home/rohit/Desktop/Day5/Ctypes/dir_5/first.so")
clib.display1()

alloc_func = clib.allocMemory
alloc_func.restype = ctypes.POINTER(ctypes.c_char_p)
dealloc_func = clib.freeMemory
dealloc_func.argtypes = [ctypes.POINTER(ctypes.c_char_p)]

cStringPointer=alloc_func()
cString=ctypes.c_char_p.from_buffer(cStringPointer)
print(cString.value)

dealloc_func(cStringPointer)
