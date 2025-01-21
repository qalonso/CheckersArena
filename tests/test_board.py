import unittest
import numpy as np
from game.board import Board

class TestBoard(unittest.TestCase):
    def test_initialize_pieces(self):
        """
        Vérifiez que les pions sont placés correctement sur le damier.

        La fonction initialize_pieces est appelée pour placer les pions sur le damier.
        Les pions blancs sont placés sur les 3 premières rangées, et les pions noirs
        sur les 3 dernières rangées.

        La fonction test_initialize_pieces vérifie que les pions sont placés
        correctement en parcourant le damier et en comparant les éléments du
        tableau self.grid avec les valeurs attendues.
        """
        board = Board()
        board.initialize_pieces()

        # Vérifiez que les pions blancs sont placés correctement
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.assertEqual(board.grid[row, col], 'wp')
                else:
                    self.assertEqual(board.grid[row, col], '')

        # Vérifiez que les pions noirs sont placés correctement
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.assertEqual(board.grid[row, col], 'bp')
                else:
                    self.assertEqual(board.grid[row, col], '')

        # Vérifiez que les cases intermédiaires sont vides
        for row in range(3, 5):
            for col in range(8):
                self.assertEqual(board.grid[row, col], '')
                
        board.print_board()

if __name__ == '__main__':
    unittest.main()
