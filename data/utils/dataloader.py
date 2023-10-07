import numpy as np
import os

class DataLoader():
    def __init__(self, instance):
        self.instance = np.load(instance)
    
    def getlen(self):
        return np.size(self.instance)
    
    def getIn(self):
        pass
    