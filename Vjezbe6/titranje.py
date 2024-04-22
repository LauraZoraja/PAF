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
        for x in self.listax_abs1:
            if self.listax_abs1.index(x) <= self.indexj:
                continue
            elif self.listax_abs1.index(x) > self.indexj:
                while x > self.listax_pomocno[-1]:
                    self.listax_pomocno.append(x)
                    if x < self.listax_pomocno[-1]:
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

        