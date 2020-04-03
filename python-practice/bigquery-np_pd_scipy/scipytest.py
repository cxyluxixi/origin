import numpy as np 

from scipy.integrate import quad,dblquad,nquad

# quad ——积分，dblquad —— 二重积分，nquad —— N重积分
print(quad(lambda x: np.exp(-x),0, np.inf))
print(dblquad(lambda x,y:np.exp(-y*x)/x**3,0,np.inf,lambda y: 1,lambda y:np.inf))

def f(x,y):
    return x*y
def a():
    return [0,0.5]
def b(y):
    return [0,1-2*y]
print(nquad(f,[a,b]))


