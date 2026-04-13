import numpy as np
import math
import pygame

def rotX(p,a): return np.dot(p,[[1,0,0],[0,math.cos(a),-math.sin(a)],[0,math.sin(a),math.cos(a)]])
def rotY(p,a): return np.dot(p,[[math.cos(a),0,math.sin(a)],[0,1,0],[-math.sin(a),0,math.cos(a)]])
def rotZ(p,a): return np.dot(p,[[math.cos(a),-math.sin(a),0],[math.sin(a),math.cos(a),0],[0,0,1]])

def shear(p, k=0.5):
    return np.dot(p, [[1,k,0],[0,1,0],[0,0,1]])

def get_transformation_matrix(angle_x, angle_y, angle_z, scale, shear_on):
    Rx = np.array([[1,0,0],[0,math.cos(angle_x),-math.sin(angle_x)],[0,math.sin(angle_x),math.cos(angle_x)]])
    Ry = np.array([[math.cos(angle_y),0,math.sin(angle_y)],[0,1,0],[-math.sin(angle_y),0,math.cos(angle_y)]])
    Rz = np.array([[math.cos(angle_z),-math.sin(angle_z),0],[math.sin(angle_z),math.cos(angle_z),0],[0,0,1]])

    S = np.array([[scale,0,0],[0,scale*1.5,0],[0,0,scale*0.5]])

    if shear_on:
        k = math.sin(pygame.time.get_ticks()*0.002)
        Sh = np.array([[1,k,0],[0.3,1,0],[0,0.5,1]])
    else:
        Sh = np.identity(3)

    return Sh @ Rz @ Ry @ Rx @ S