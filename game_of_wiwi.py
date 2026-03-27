import time
import pygame
import numpy as np

#Color Variables
COLOR_BG = (10, 10, 10)
COLOR_GRID = (50, 50, 50)
COLOR_DIE_NEXT = (255, 10, 75)
COLOR_ALIVE_NEXT = (10, 255, 75)

#Function that updates cells. (Main function/Logic of the game)
def update(screen, cells, size, with_progress=False):
	updated_cells = np.empty((cells.shape[0], cells.shape[1]))

