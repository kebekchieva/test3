class Envelope:
    def __init__(self, a, b):
        self.square = a * b

class Box:
    def __init__(self, a, b, c):
        self.square = 2 * c * (a + b)
        self.envelope = []
    def addEnv(self, k, l):
        self.Env.append(Envelope(k, l))

env1 = Box(1, 2, 5)
print(env1.square)
env1.addEnv(5, 1)