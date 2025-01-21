import numpy as np

class Board:
    def __init__(self):
        """
        Initialisation du damier.

        La grille du damier est initialisée avec des cases vides.
        Les pions sont placés sur les cases noires du damier.
        """
        self.grid = np.full((8, 8), '', dtype=object)
        self.initialize_pieces()

    def initialize_pieces(self):
        """
        Initialise les pions sur le damier.

        La fonction parcourt le damier et place les pions sur les cases noires.
        Les pions blancs sont placés sur les 3 premières rangées, et les pions
        noirs sur les 3 dernières rangées.
        """
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 1:  # Vérifie si la case est noire
                    if row < 3:
                        self.grid[row, col] = 'wp'  # Pions blancs
                    elif row > 4:
                        self.grid[row, col] = 'bp'  # Pions noirs

    def print_board(self):
        """
        Affiche le damier dans la console.

        La fonction parcourt le damier et affiche les cases ligne par ligne.
        Les cases noires contenant des pions sont affichées avec le symbole des pions.
        Les cases blanches sont affichées vides.
        """
        for row in self.grid:
            print(' '.join(row))
    
    # Move a piece from start to end
    def move_piece(self, start, end):
        pass
    
    # Check if a move is valid
    def is_valid_move(self, start, end):
        pass