import random
from random import randint
from pprint import pprint


class Board:
    """ 
    Define game's board
    """
    def __init__(self, size, num_ships, name, type):
        self.size = [["-" for i in range(size)] for row in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type

    def print(self):
        for row in self.size:
            board = " ".join(row)
        for landpoint in range(1, 9):
            print(landpoint, board)


    def column_cordenates():
        translate_cordenates = {
            "a" : 0, "b": 1, "c": 2, "d": 3, "f": 4, "g": 5, "h": 6, "i": 7
            }
        return translate_cordenates


def main():
    
    board = Board(8, 8, "Javier", "user")
    board.print()
    # Board.column_cordenates()

print("  A B C D F G H I")
main()
