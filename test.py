import unittest
from pawn import *
from strategy import *

##     utility functions    ##
class quoridor_position(unittest.TestCase):
    def test_position0(self):
        actual = position(2)
        esperado = ((0, 2))
        self.assertEqual(actual,esperado)

    def test_position1(self):
        actual = position(288)
        esperado = ((16, 16))
        self.assertEqual(actual,esperado)
    
    def test_position2(self):
        actual = position(36)
        esperado = ((2, 2))
        self.assertEqual(actual,esperado)

class quoridor_identify(unittest.TestCase):
    def test_identify(self):
        board = "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  "
        actual_turn = "N"
        actual = identify(board,actual_turn)
        esperado = [2,8,14]
        self.assertEqual(actual,esperado)

class quoridor_pawnmovedown(unittest.TestCase):
    def test_pawnmovedown1(self):
        board = "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  "
        actual_turn = "N"
        pc=2
        actual = pawnmovedown(board,actual_turn,pc)
        esperado = ((0, 2), (2, 2))
        self.assertEqual(actual,esperado)
    def test_pawnmovedown2(self):
        board = "  N     N     N  -*-                                                                                                                                                                                                                                                              S     S     S  "
        actual_turn = "N"
        pc=2
        actual = pawnmovedown(board,actual_turn,pc)
        esperado = None
        self.assertEqual(actual,esperado)   
    def test_pawnmovedown3(self):
        board = "  N     N     N                     S                                                                                                                                                                                                                                             S     S     S  "
        actual_turn = "N"
        pc=2
        actual = pawnmovedown(board,actual_turn,pc)
        esperado = ((0, 2), (4, 2))
        self.assertEqual(actual,esperado)

class quoridor_pawnmoveleft(unittest.TestCase):    
    def test_pawnmoveleft1(self):
        board = "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  "
        actual_turn = "N"
        pc=2
        actual = pawnmoveleft(board,actual_turn,pc)
        esperado = ((0, 2), (0, 0))
        self.assertEqual(actual,esperado)

class quoridor_pawnmoveright(unittest.TestCase): 
    def test_pawnmoveright1(self):
        board = "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  "
        actual_turn = "N"
        pc=2
        actual = pawnmoveright(board,actual_turn,pc)
        esperado = ((0, 2), (0, 4))
        self.assertEqual(actual,esperado)

class quoridor_pawnmoveup(unittest.TestCase): 
    def test_pawnmoveup1(self):
        board = "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  "
        actual_turn = "S"
        pc=274
        actual = pawnmoveup(board,actual_turn,pc)
        esperado = ((16, 2), (14, 2))
        self.assertEqual(actual,esperado)

class quoridor_distance(unittest.TestCase): 
    def test_distance1(self):
        board = "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  "
        actual_turn = "N"
        pcs=2
        actual = distance(board,actual_turn,pcs)
        esperado = 8
        self.assertEqual(actual,esperado)
    def test_distance2(self):
        board = "  N     N     N                                                                                                          -                                                                                                                                                        S     S     S  "
        actual_turn = "N"
        pcs=2
        actual = distance(board,actual_turn,pcs)
        esperado = 9
        self.assertEqual(actual,esperado)

class quoridor_walldown(unittest.TestCase): 
    def test_walldown1(self):
        board = "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  "
        actual_turn = "N"
        pc=2
        actual = walldown(board,actual_turn,pc)
        esperado = 1
        self.assertEqual(actual,esperado)
    def test_walldown2(self):
        board = "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  "
        actual_turn = "N"
        pc=240
        actual = walldown(board,actual_turn,pc)
        esperado = 1
        self.assertEqual(actual,esperado)

class quoridor_mindist(unittest.TestCase): 
    def test_mindist1(self):
        board = "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  "
        actual_turn = "N"
        actual = mindist(board,actual_turn)
        esperado = 2
        self.assertEqual(actual,esperado)
    def test_mindist2(self):
        board = "  N     N     N                                                                                                          -                                                                                                                                                        S     S     S  "
        actual_turn = "N"
        actual = mindist(board,actual_turn)
        esperado = 8
        self.assertEqual(actual,esperado)

if __name__ == "__main__":
    unittest.main()
