import math

def convertCtoF(x):
    return (x*1.8)+32

def areaCircle(r):
    return math.pi*(r**2)
    
def areaTriangle(x1,y1,x2,y2,x3,y3):
    return 0.5*abs((x1*(y2+y3))+(x2*(y1+y3))+(x3*(y1+y2)))
