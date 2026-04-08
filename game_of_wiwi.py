import time
import pygame
import numpy as np

#Color Variables
COLOR_BG = (10, 10, 10)
COLOR_GRID = (50, 50, 50)
COLOR_DIE_NEXT = (255, 10, 75)
COLOR_ALIVE_NEXT = (0, 255, 255)

#Function that updates cells. (Main function/Logic of the game)
def update(screen, cells, size, with_progress=False):
	updated_cells = np.zeros((cells.shape[0], cells.shape[1])) #Creates shape of the alreaddy existed cells.

	for row, col in np.ndindex(cells.shape): #Takes each individual cell that alreaddy exists and applies rules of the game to it.
		alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
		color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

		if cells[row, col] == 1:
			if alive < 2 or alive > 3:
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
	return updated_cells
def main(): #main function of code
	pygame.init()
	screen = pygame.display.set_mode((800, 600)) #creates screen size

	cells = np.zeros((60, 80))
	screen.fill(COLOR_GRID)
	update(screen, cells, 10)

	pygame.display.flip()
	pygame.display.update() #Creaters starter screen

	running = False

	while True: #Loop that checks when the player hits one of the following keys.
		for event in pygame.event.get():
			if event.type == pygame.QUIT: #allows player to quit game
				pygame.quit()
				return
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE: #pauses game when player hits space, or unpauses it
					running = not running
					update(screen, cells, 10)
					pygame.display.update()
			if pygame.mouse.get_pressed()[0]: #creates cells when player clicks
				pos = pygame.mouse.get_pos()
				cells[pos[1] // 10, pos[0] // 10] = 1
				update(screen, cells, 10)
				pygame.display.update()

		screen.fill(COLOR_GRID) #Fills the backgrond with said color

		if running:
			cells = update(screen, cells, 10, with_progress=True)
			pygame.display.update()
		time.sleep(0.001) #rate it updates the game

if __name__ == '__main__':
	main() #genuinely main line of code that runs this script