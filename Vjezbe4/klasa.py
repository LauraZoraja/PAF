class Particle:
    def __init__(self, masa, x0, v):
        self.masa = masa
        self.x0 = x0
        self.v = v

    def print_info(self):
        print('Masa cestice iznosi {}.'.format(self.masa))
        print('Polozaj cestice je {}.'.format(self.x0))
        print('Brzina cestice je {}.'.format(self.v))

    def move_to_0(self):
        self.x0 = 0

    def change_velocity(self, delta_v):
        self.v += delta_v

p1 = Particle(10,10,20)
#print('Masa cestice iznosi {} g.'.format(p1.masa))
#print('Polozaj cestice je {} cm.'.format(p1.x0))
p1.print_info()
p1.move_to_0()
p1.change_velocity(5)
p1.print_info()