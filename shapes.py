import numpy as np
import math

def cube():
    v=[[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],
       [-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1]]
    e=[(0,1),(1,2),(2,3),(3,0),
       (4,5),(5,6),(6,7),(7,4),
       (0,4),(1,5),(2,6),(3,7)]
    return np.array(v),e

def pyramid():
    v=[[0,1,0],[-1,-1,-1],[1,-1,-1],[1,-1,1],[-1,-1,1]]
    e=[(0,1),(0,2),(0,3),(0,4),
       (1,2),(2,3),(3,4),(4,1)]
    return np.array(v),e

def tetra():
    v=[[1,1,1],[-1,-1,1],[-1,1,-1],[1,-1,-1]]
    e=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    return np.array(v),e

def octa():
    v=[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
    e=[(0,2),(0,3),(0,4),(0,5),
       (1,2),(1,3),(1,4),(1,5),
       (2,4),(2,5),(3,4),(3,5)]
    return np.array(v),e

def prism():
    v=[[-2,-1,-1],[2,-1,-1],[2,1,-1],[-2,1,-1],
       [-2,-1,1],[2,-1,1],[2,1,1],[-2,1,1]]
    e=[(0,1),(1,2),(2,3),(3,0),
       (4,5),(5,6),(6,7),(7,4),
       (0,4),(1,5),(2,6),(3,7)]
    return np.array(v),e

def tri_prism():
    return pyramid()

def pent_prism():
    v=[]; e=[]
    for i in range(5):
        a=2*math.pi*i/5
        v.append([math.cos(a),math.sin(a),-1])
    for i in range(5):
        a=2*math.pi*i/5
        v.append([math.cos(a),math.sin(a),1])
    for i in range(5):
        e.append((i,(i+1)%5))
        e.append((i+5,(i+1)%5+5))
        e.append((i,i+5))
    return np.array(v),e

def cylinder():
    v=[]; e=[]
    for i in range(0,360,30):
        a=math.radians(i)
        v.append([math.cos(a),math.sin(a),-1])
        v.append([math.cos(a),math.sin(a),1])
    n=len(v)
    for i in range(0,n,2):
        e.append((i,(i+2)%n))
        e.append((i+1,(i+3)%n))
        e.append((i,i+1))
    return np.array(v),e

def cone():
    v=[[0,0,1]]; e=[]
    for i in range(0,360,30):
        a=math.radians(i)
        v.append([math.cos(a),math.sin(a),-1])
    for i in range(1,len(v)):
        e.append((0,i))
    return np.array(v),e

def sphere():
    v=[]
    for i in range(0,180,30):
        for j in range(0,360,30):
            v.append([
                math.sin(math.radians(i))*math.cos(math.radians(j)),
                math.sin(math.radians(i))*math.sin(math.radians(j)),
                math.cos(math.radians(i))
            ])
    v=np.array(v)
    e=[(i,i+1) for i in range(len(v)-1)]
    return v,e