class particle:
    import matplotlib.pyplot as plt
    def __init__(self, x0, y0, v0, kut):
        import numpy as np
        self.x0 = x0
        self.y0 = y0
        self.v0 = v0
        kut = np.radians(kut)
        self.kut = kut
        self.vxi = self.v0*np.cos(self.kut)
        self.vyi = self.v0*np.sin(self.kut)
        self.ax = 0.
        self.ay = 9.81
    def reset(self):
        import numpy as np
        self.x0 = 0.
        self.y0 = 0.
        self.v0 = 0.
        self.kut = np.rad(0.)

    def __move(self, dt = 0.01):
        self.x2i = self.xi + self.vxi*dt
        self.xi = self.x2i
        self.y2i = self.yi + self.vyi*dt
        self.yi = self.y2i

        self.vx2i = self.vxi + self.ax*dt
        self.vxi = self.vx2i
        self.vy2i = self.vyi - self.ay*dt
        self.vyi = self.vy2i


    def range(self):
        self.listaxi = []
        self.listayi = []
        self.yi = self.y0
        self.xi = self.x0
        while self.yi >= 0.:
            self.__move()
            self.listayi.append(self.yi)
            self.listaxi.append(self.xi)
            if self.yi == 0.:
                break

        print(self.listaxi[-1] - self.x0)

    def plot_trajectory(self):
        import matplotlib.pyplot as plt
        import numpy as np
        self.range()
        plt.plot(self.listaxi,self.listayi,'b')
        plt.xticks(np.arange(0,float(round(self.listaxi[-1]))+1.,step=1))
        plt.title('Putanja cestice')
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.grid()
        plt.show()


p1 = particle(3,4,10,45)
p1.plot_trajectory()