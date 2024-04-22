import matplotlib.pyplot as plt
import numpy as np

class HarmonicOscillator:
    def __init__(self,k,m,xi = 0,vi = 0):
        self.k = k
        self.m = m
        self.xi = xi
        self.ai = -(k/m)*self.xi
        self.vi = vi
        self.listax = [self.xi]
        self.listav = [self.vi]
        self.listaa = [self.ai]
        self.listat = [0]
    def move(self):
        
        self.vi += self.ai*self.dt
        self.xi += self.vi*self.dt
        self.ai = -(self.k/self.m)*self.xi
        
        
        #self.vi = self.v2i
        #self.xi = self.x2i
        #self.ai = self.a2i

    def oscilate(self,t,dt = 0.01):
        self.t = t
        self.dt = dt
        self.T = 0
        while self.T < self.t:
            self.T += self.dt
            self.move()
            self.listav.append(self.vi)
            self.listax.append(self.xi)
            self.listaa.append(self.ai)
            self.listat.append(self.T)

    def plot(self):
        plt.subplot(3,1,1) #jedan redak, tri stupca, prvi graf
        plt.plot(self.listat,self.listax,'o',markersize = 1)
        plt.xlabel("t [s]")
        plt.ylabel('x [m]')
        plt.yticks(np.arange(round(min(self.listax),1),round(max(self.listax)+0.1,1),0.1))
        plt.grid()
        plt.title("Harmonic oscillator")

        plt.subplot(3,1,2)
        plt.plot(self.listat,self.listav,'o',markersize = 1)
        plt.xlabel("t [s]")
        plt.ylabel('v [m/s]')
        plt.yticks(np.arange(round(min(self.listav)),round(max(self.listav)+1),1))
        plt.grid()

        plt.subplot(3,1,3)
        plt.plot(self.listat,self.listaa,'o',markersize = 1, label = 'dt = {}'.format(self.dt))
        plt.xlabel("t [s]")
        plt.ylabel('a [m/$s^2$]')
        plt.yticks(np.arange((round(min(self.listaa)+9)//10 * 10),round(max(self.listaa)),10))
        plt.grid()

    def plot_reset(self):
        self.xi = self.listax[0]
        self.ai = self.listaa[0]
        self.vi = self.listav[0]
        self.listax = [self.xi]
        self.listav = [self.vi]
        self.listaa = [self.ai]
        self.listat = [0]


    #def plotx(self,t,dt = 0.01):
        #self.oscilate(t,dt)
        #self.t = t
        #self.dt = dt
        #plt.plot(self.listat,self.listax,'o',markersize = 3)
        #plt.title('Putanja cestice')
        #plt.xlabel('t [s]')
        #plt.ylabel('x [m]')
    

    def show(self):
        plt.legend()
        plt.show()

    def period(self,t,dt = 0.01):
        self.t = t
        self.dt = dt
        self.oscilate(t,dt)
        self.listax_abs1 = []
        self.listax_pomocno = [self.listax[0]]
        self.lista_period = []
        T = 0
        for i in self.listax:
            i = abs(i)
            self.listax_abs1.append(i)
        for j in self.listax_abs1:
            while j < self.listax_pomocno[-1]:
                self.listax_pomocno.append(j)
                if j > self.listax_pomocno[-1]:
                    break
        self.indexj = len(self.listax_pomocno)
        print(self.listax_pomocno)
        for z in self.listax_abs1:
            for x in range(self.indexj + 1,len(self.listax_abs1)):
                if x <= self.indexj:
                    continue
                elif x < self.indexj:
                    while z < self.listax_pomocno[-1]:
                        self.listax_pomocno.append(x)
                        if z > self.listax_pomocno[-1]:
                            break
        print(self.listax_pomocno)
        #print(self.listax)
        self.indexk = len(self.listax_pomocno)
        print(self.indexj,self.indexk)
        for x in range(self.indexj,self.indexk):
            self.lista_period.append(self.listat[x])
        #T = self.lista_period[-1] - self.lista_period[0]
        #print(np.radians(T))
        print(T)





h1 = HarmonicOscillator(10,0.1,0.3,2)
h1.oscilate(2)
h1.plot()
h1.plot_reset()
h1.oscilate(2,0.001)
h1.plot()
h1.plot_reset()
h1.oscilate(2,0.05)
h1.plot()
h1.plot_reset()
h1.show()

h1.period(2)
h1.period(2,0.001)
h1.period(2,0.05)