import pygame
from game.board import Board

class Display:
    def __init__(self, screen):
        self.screen = screen
        self.board = Board()
        self.draw_board()
        self.draw_pieces()

    def draw_board(self):
        # Dessiner le damier
        for row in range(8):
            for col in range(8):
                x, y = col * 100, row * 100
                color = (0, 0, 0) if (row + col) % 2 == 1 else (255, 255, 255)
                pygame.draw.rect(self.screen, color, (x, y, 100, 100))

    def draw_pieces(self):
        # Dessiner les pions
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row, col]
                if piece:
                    x, y = col * 100 + 50, row * 100 + 50
                    color = (255, 255, 255) if piece == 'wp' else (100, 100, 100)
                    pygame.draw.circle(self.screen, color, (x, y), 40)

    def draw(self, board):
        self.board = board
        self.screen.fill((0, 0, 0))  # Effacer l'écran
        self.draw_board()
        self.draw_pieces()
