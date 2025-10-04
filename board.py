import sys
import pygame
import random
import numpy as np
from kernel import Kernel

def main():
    b = Board((1000,1000),Kernel.parse(sys.argv[1]))
    b.run()

class Board:
    def __init__(self,dims,kernel):
        self.screen = pygame.display.set_mode(dims,pygame.RESIZABLE)#|pygame.SCALED)
        self.cell_size = 20
        self.offset = [0,0]
        
        pygame.init()

        self.alive = set([(i,j) for i in range(dims[1]//self.cell_size) for j in range(dims[0]//self.cell_size) if random.random() > .5])
        self.kernel = kernel

    def evolve(self):
        self.alive = self.kernel.update(self.alive)

    def display(self):
        w,h = self.screen.get_size()
        board = np.zeros((h//self.cell_size,w//self.cell_size), dtype=int)

        for (i,j) in self.alive:
            i -= self.offset[0]
            j -= self.offset[1]
            if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]):
                board[i][j] = 1

        surface = pygame.surfarray.make_surface(255*board.T)
        self.screen.blit(pygame.transform.scale(surface, (w,h)), (0,0))

        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        paused = True
        x,y = 0,0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = not paused
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_r:
                        w,h = self.screen.get_size()
                        self.alive = set([(i+self.offset[0],j+self.offset[1]) for i in range(h//self.cell_size) for j in range(w//self.cell_size) if random.random() > .5])
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x,y = pygame.mouse.get_pos()
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    x2,y2 = pygame.mouse.get_pos()
                    # Addd logic to fill a rectangle with random
                                
            keys = pygame.key.get_pressed()
            if keys[pygame.K_EQUALS]:
                self.cell_size += 1
            if keys[pygame.K_MINUS]:
                self.cell_size = max(1,self.cell_size-1)
            if keys[pygame.K_DOWN]:
                self.offset[0] += 20//self.cell_size
            if keys[pygame.K_UP]:
                self.offset[0] -= 20//self.cell_size
            if keys[pygame.K_LEFT]:
                self.offset[1] -= 20//self.cell_size
            if keys[pygame.K_RIGHT]:
                self.offset[1] += 20//self.cell_size
            
            if not paused:
                self.evolve()
            self.display()

            clock.tick(24)

if __name__ == '__main__':
    main()
