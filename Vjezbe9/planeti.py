import numpy as np
import matplotlib.pyplot as plt

import pdb
#pdb.set_trace()
class planet:

    def __init__(self, t = 365.242 * 24. * 3600., ms = 1.989*10.**30., mz = 5.9742*10.**24., G =  6.67408*10.**(-11.), dt = 3600., xz = 1.486*10.**11., vz = 29783.):
        self.t = t
        self.ms = ms
        self.mz = mz
        self.G = G
        self.dt = dt
        self.rz = np.array((xz,0.),dtype=float)
        self.rs = np.array((0.,0.),dtype=float)
        self.vz = np.array((0.,vz),dtype=float)
        self.vs = np.array((0.,0.),dtype=float)
        self.xz = xz
        self.yz = 0.
        self.dz = ((self.rz-self.rs)[0]**2. + (self.rz-self.rs)[1]**2.)**0.5
        self.listarzx = [self.rz[0]]
        self.listarzy = [self.rz[1]]

    def move(self):
        #pdb.set_trace()
        self.F = (-self.G*self.mz*self.ms/(self.dz**3.))*(self.rz-self.rs)
        self.az = self.F/self.mz
        self.asu = self.F/self.ms
        self.vz += self.az*self.dt
        self.vs += self.asu*self.dt
        self.rz += self.vz*self.dt
        self.rs += self.vs*self.dt
        self.dz = ((self.rz-self.rs)[0]**2. + (self.rz-self.rs)[1]**2.)**0.5

    def godina(self):
        T = 0
        self.listarz = [np.copy(self.rz)]
        self.listars = [np.copy(self.rs)]
        self.listaa = []
        self.listavz = []
        while T < self.t:
            self.move()
            self.listarz.append(np.copy(self.rz))
            self.listars.append(np.copy(self.rs))
            self.listaa.append(self.az)
            self.listavz.append(self.vz)
            T += self.dt
            #pdb.set_trace()
            #print(self.az,self.vz,self.xz)

    def plot(self):
        plt.plot([x[0] for x in self.listarz], [x[1] for x in self.listarz], label = 'Earth')
        plt.plot([x[0] for x in self.listars], [x[1] for x in self.listars],'o',color = 'yellow', markersize = 4, label = 'Sun')
        plt.xlabel("x [m]")
        plt.ylabel('y [m]')
        plt.title("x-y graf")
        plt.axis('equal')
        plt.legend()
        plt.title('Sun-Earth system')
        plt.axis('square')
        plt.show()

h1 = planet()
h1.godina()
h1.plot()