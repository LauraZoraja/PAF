import matplotlib.pyplot as plt
import numpy as np

class projectile:
    def __init__(self,t,m,xi,yi,vi,kut,rho,C,A,dt = 0.01,metoda = 'euler'):
        self.t = t
        self.m = m
        self.x = xi
        self.y = yi
        self.kut = np.radians(kut)
        self.rho = rho
        self.C = C
        self.A = A
        self.g = 9.81
        self.dt = dt
        self.metoda = metoda
        self.vx = vi*np.cos(self.kut)
        self.vy = vi*np.sin(self.kut)
        self.ax = -np.sign(self.vx)*((rho*C*A)/2*self.m)*(self.vx)*2
        self.ay = -self.g -np.sign(self.vy)*((rho*C*A)/2*self.m)*(self.vy)*2
        self.listax = [self.x]
        self.listay = [self.y]
        self.listavx = [self.vx]
        self.listavy = [self.vy]
        self.listaax = [self.ax]
        self.listaay = [self.ay]
        self.listat = [0]

    def move(self):
        
        self.vx += self.ax*self.dt
        self.vy += self.ay*self.dt
        self.x += self.vx*self.dt
        self.y += self.vy*self.dt
        self.ax = -np.sign(self.vx)*((self.rho*self.C*self.A)/2*self.m)*(self.vx)*2
        self.ay = -self.g -np.sign(self.vy)*((self.rho*self.C*self.A)/2*self.m)*(self.vy)*2

    def euler(self,dt = 0.01):
        self.T = 0
        self.dt = dt
        while self.T < self.t:
            self.T += self.dt
            self.move()
            self.listavx.append(self.vx)
            self.listavy.append(self.vy)
            self.listax.append(self.x)
            self.listay.append(self.y)
            self.listaax.append(self.ax)
            self.listaay.append(self.ay)
            self.listat.append(self.T)

    def runge():
        return 0

    def plot(self):
        plt.plot(self.listax,self.listay,'o',markersize = 1, label = 'dt = {},{}'.format(self.dt,self.metoda))
        plt.xlabel("x [m]")
        plt.ylabel('y [m]')
        plt.grid()
        plt.title("x-y graf")

    def plot_reset(self):
        self.x = self.listax[0]
        self.y = self.listay[0]
        self.ax = self.listaax[0]
        self.ay = self.listaay[0]
        self.vx = self.listavx[0]
        self.vy = self.listavy[0]
        self.listax = [self.x]
        self.listay = [self.y]
        self.listavx = [self.vx]
        self.listavy = [self.vy]
        self.listaax = [self.ax]
        self.listaay = [self.ay]
        self.listat = [0]

    def show(self):
        plt.legend()
        plt.show()

h1 = projectile(2,2,0,0,15,45,1,0,3)
h1.euler()
h1.plot()
h1.plot_reset()
h1.euler(0.001)
h1.plot()
h1.plot_reset()
h1.euler(0.05)
h1.plot()
h1.plot_reset()
h1.show()