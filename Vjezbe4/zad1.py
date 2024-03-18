class particle:
    import matplotlib.pyplot as plt
    def __init__(self, x0, y0, v0, kut):
        import numpy as np
        self.x0 = x0
        self.y0 = y0
        self.v0 = v0
        kut = np.radians(kut)
        self.kut = kut

    def reset(self):
        import numpy as np
        self.x0 = 0
        self.y0 = 0
        self.v0 = 0
        self.kut = np.rad(0)

    def __move(self, dt = 0.01):
        import numpy as np
        self.vx0 = self.v0*np.cos(self.kut)
        self.vy0 = self.v0*np.sin(self.kut)
        self.ax = 0
        self.ay = -9.81
        self.vxi = self.vx0 + self.ax*dt
        self.vyi = self.vy0 + self.ay*dt
        self.xi = self.x0 + self.vxi*dt
        self.yi = self.y0 + self.vyi*dt
        print(self.vxi, self.vyi, self.xi, self.yi)

    def range(self):
        listaxi = []
        self.yi = self.y0
        while self.yi >= self.y0:
            self.__move(self)
            listaxi.append(self.xi)
        print(listaxi[-1])


p1 = particle(3,4,10,45)
p1.range()