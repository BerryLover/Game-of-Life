
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

class ConwayWorld:
    
    def __init__(self, world_size):
        self.size = world_size
        self.matrix = np.zeros(shape=(world_size, world_size))
        
    def RandomSeed(self, population_rate):
        self.matrix = np.random.rand(self.size, self.size)
        for row in range(self.size):
            for col in range(self.size):
                if (self.matrix[row][col] >=0 and self.matrix[row][col] < population_rate):
                    self.matrix[row][col] = 1
                elif (self.matrix[row][col] >= population_rate and self.matrix[row][col] <1):
                    self.matrix[row][col] = 0
                else:
                    print("Error: Matrix element value exceed range limit! Exit")
                    return -1
        rand_matrix = self.matrix.copy()
        return rand_matrix
    
    def Evolve(self):
        new_matrix = self.matrix.copy()
        for row in range(self.size):
            for col in range(self.size):
                total_alive_cell = self.matrix[(row-1)%self.size][(col-1)%self.size] \
                                + self.matrix[(row-1)%self.size][(col)%self.size] \
                                + self.matrix[(row-1)%self.size][(col+1)%self.size] \
                                + self.matrix[(row)%self.size][(col-1)%self.size] \
                                + self.matrix[(row)%self.size][(col+1)%self.size] \
                                + self.matrix[(row+1)%self.size][(col-1)%self.size] \
                                + self.matrix[(row+1)%self.size][(col)%self.size] \
                                + self.matrix[(row+1)%self.size][(col+1)%self.size]
                if self.matrix[row][col] == 0:
                    if total_alive_cell == 3:
                        new_matrix[row][col] = 1
                    elif (total_alive_cell >=0 and total_alive_cell <= 8 and total_alive_cell != 3):
                        pass
                    else:
                        print("Error: New value assignment exceed range limit! Exit")
                        return -1
                elif self.matrix[row][col] == 1:
                    if (total_alive_cell >=0 and total_alive_cell < 2):
                        new_matrix[row][col] = 0
                    elif (total_alive_cell == 2 or total_alive_cell ==3):
                        pass
                    elif (total_alive_cell > 3 and total_alive_cell <= 8):
                        new_matrix[row][col] = 0
                    else:
                        print("Error: New value assignment exceed range limit! Exit")
                        return -1
        self.matrix = new_matrix.copy()
        
        #print("NEW!!\n", self.matrix)
        return new_matrix
    
    def DrawIteration(self, frame):
        new_matrix = self.Evolve()
        img.set_data(new_matrix)
        return img
    
 
'''
def DrawIteration(frame, img, instance):
    new_matrix = instance.Evolve()
    print("NEW MATRIX IS \n\n", new_matrix)
    img.set_data(new_matrix)
    return img    
'''  
    
if __name__ == "__main__":
    world_size = 100
    world_01 = ConwayWorld(world_size)
    print(world_01.matrix)
    world_01.RandomSeed(0.66)
    print(world_01.matrix)
  
    
    fig, ax = plt.subplots()
    img = ax.imshow(world_01.matrix)
    #ax.imshow([[[1,1,1],[100,100,100]],[[24,65,100],[33,122,23]]])

    anim = animation.FuncAnimation(fig, world_01.DrawIteration, frames=200, interval=100, \
                                   blit=False, repeat = True)
    #anim.save('basic_animation.mp4', fps=25, extra_args=['-vcodec', 'libx264'])
    anim.save('gameoflife.gif', writer='imagemagick', fps=10)
    plt.show()