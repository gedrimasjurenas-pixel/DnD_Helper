class Stats:
    def __init__(self, STR=10, DEX=10, CON=10, INT=10, WIS=10, CHA=10):
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA

    @property
    def con(self):
        return self.CON

    def update(self, stat, value):
        if hasattr(self, stat):
            setattr(self, stat, value)
