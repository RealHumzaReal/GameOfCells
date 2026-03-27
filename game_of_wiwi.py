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
	updated_cells = np.empty((cells.shape[0], cells.shape[1])) #Creates shape of the alreaddy existed cells.

	for row, col in np.ndindex(cells.shape): #Takes each individual cell that alreaddy exists and applies rules of the game to it.
		alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
		color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

		if cells[row, col] == 1:
			if alive < 2 or alive > 3
				if with_progress:
					color = COLOR_DIE_NEXT
			elif 2 <= alive <= 3:
				updated_cells[row, col] = 1
				if with_progress:
					color = COLOR_ALIVE_NEXT
		else:
			if alive == 3:
				updated_cells[row, col] = 1
				if with_progress:
					color = COLOR_ALIVE_NEXT

		pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1)) #Draws cells onto the chart (Visual aspect)
	return_updated_cells