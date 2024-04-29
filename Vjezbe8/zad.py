import numpy as np
import matplotlib as plt

class moving_particle:
    def __init__(self, t, vx, vy, vz, Ex, Ey, Ez, x = 0, y = 0, z = 0, dt = 0.01, Bx = 0, By = 0,Bz = 1, m = 9.109 * 10**(-31), q = -1):
        self.m = m
        self.q = q
        self.dt = dt
        self.t = t
        self.v = np.array((vx,vy,vz))
        self.E = np.array((Ex,Ey,Ez))
        self.B = np.array((Bx,By,Bz))
        self.position = np.array((x,y,z))
        self.F = self.q * (self.E + np.cross(self.v,self.B))

    def move(self):
        self.a = self.F / self.m
        self.v += self.a*self.dt
        self.position += self.v*self.dt

    def vekt(self):
        return 0