import matplotlib.pyplot as plt
import numpy as np

class MyGrid:
    size = 4

    def __init__(self, size=4):
        self.size = size
        print("Start grid with size", self.size)

    def drawGrid(self):
        x = np.array([0, 1, 2, 3])
        y = np.array([0, 1, 2, 3])
        X, Y = np.meshgrid(x, y)    
        plt.plot(X, Y, marker='o', color='b', linestyle='none')
        plt.title('Simulation Grid')
        plt.show()



    # def drawGrid(self):
    #     plt.figure(figsize=(self.size, self.size))
    #     plt.plot(range(1), [1])
    #     plt.title('Simulation Grid')
    #     plt.xlabel('Index')
    #     plt.ylabel('Value')
    #     plt.grid(True)
    #     plt.legend()
    #     plt.show()