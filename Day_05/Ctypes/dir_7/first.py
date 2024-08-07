import ctypes
clib = ctypes.CDLL("/home/rohit/Desktop/Day5/Ctypes/dir_7/first.so")

class Point(ctypes.Structure):
    _fields_ = [("x",ctypes.c_int),("z",ctypes.c_int)]

p = Point(5,6)
print(p.x,p.z)

clib.printPoint(p)

clib.getPoint.restype = ctypes.POINTER(Point)
p1=clib.getPoint()
print(p1.contents.x, p1.contents.z)
