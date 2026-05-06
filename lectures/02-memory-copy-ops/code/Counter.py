class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

    def __repr__(self):
        return str(self.value)


c = Counter()
c.inc()
c.inc()

print(c)
