import unittest
from pawn import *
from strategy import *
from wall import *
# pawns    ##
class quoridor_position(unittest.TestCase):
    def test_position0(self):
        actual = position(2)
        esperado = ((0, 1))
        self.assertEqual(actual,esperado)
    def test_position1(self):
        actual = position(288)
        esperado = ((8, 8))
        self.assertEqual(actual,esperado)
    def test_position2(self):
        actual = position(36)
        esperado = ((1, 1))
        self.assertEqual(actual,esperado)
    def test_position3(self):
        actual = position(254)
        esperado = ((7, 8))
        self.assertEqual(actual,esperado)
    def test_position4(self):
        actual = position(1)
        esperado = ((0, 0))
        self.assertEqual(actual,esperado)
    def test_position5(self):
        actual = position(204)
        esperado = ((6, 0))
        self.assertEqual(actual,esperado)
    def test_position6(self):
        actual = position(0)
        esperado = ((0, 0))
        self.assertEqual(actual,esperado)
    def test_position7(self):
        actual = position(186)
        esperado = ((5, 8))
        self.assertEqual(actual,esperado)
class quoridor_pawnmovedown(unittest.TestCase):
    def test_pawnmovedown1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pc=2
        actual = pawnmovedown(request_data,pc)
        esperado = ((0, 1), (1, 1))
        self.assertEqual(actual,esperado)
    def test_pawnmovedown2(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                     S                                                                                                                                                                                                                                             S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pc=2
        prt(request_data)
        actual = pawnmovedown(request_data,pc)
        esperado = ((0, 1), (2, 1))
        self.assertEqual(actual,esperado)
class quoridor_pawnmoveleft(unittest.TestCase):    
    def test_pawnmoveleft1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pc=2
        actual = pawnmoveleft(request_data,pc)
        esperado = ((0, 1), (0, 0))
        self.assertEqual(actual,esperado)
class quoridor_pawnmoveright(unittest.TestCase): 
    def test_pawnmoveright1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pc=2
        actual = pawnmoveright(request_data,pc)
        esperado = ((0, 1), (0, 2))
        self.assertEqual(actual,esperado)
class quoridor_pawnmoveup(unittest.TestCase): 
    def test_pawnmoveup1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "S", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pc=274
        actual = pawnmoveup(request_data,pc)
        esperado = ((8, 1), (7, 1))
        self.assertEqual(actual,esperado)
# walls ****************************************************
class quoridor_walldown(unittest.TestCase): 
    def test_walldown1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pc=2
        actual = walldown(request_data,pc)
        esperado = 1
        self.assertEqual(actual,esperado)
    def test_walldown2(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        pc=240
        actual = walldown(request_data,pc)
        esperado = 1
        self.assertEqual(actual,esperado)
# class quoridor_putwall(unittest.TestCase): esta en modo random.
# strategy *************************************************
class quoridor_mindist(unittest.TestCase): 
    def test_mindist1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        actual = mindist(request_data)
        esperado = 2
        self.assertEqual(actual,esperado)
    def test_mindist2(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                          -                                                                                                                                                        S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        actual = mindist(request_data)
        esperado = 8
        self.assertEqual(actual,esperado)
class quoridor_move(unittest.TestCase): 
    def test_move1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (0,1),(1,1)
        self.assertEqual(actual,esperado)
    def test_move1(self):
        request_data={"event": "your_turn", "data": {"player_2": "armandogerman@hotmail.com", "board": "        N     N                     N                                                                      |                *                |                                                                                                                           S     S     S  ", "walls": 9.0, "score_2": 3.0, "side": "S", "player_1": "armandogerman@hotmail.com", "remaining_moves": 197.0, "score_1": -8.0, "turn_token": "cf6df257-c4b4-4102-a08b-d8ab06572529", "game_id": "c20239da-d716-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (0,1),(1,1)
        self.assertEqual(actual,esperado)

if __name__ == "__main__":
    unittest.main()