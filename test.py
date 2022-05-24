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
        actual = position(4)
        esperado = ((0, 2))
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
    def test_position8(self):
        actual = position(150)
        esperado = ((4, 7))
        self.assertEqual(actual,esperado)
    def test_position9(self):
            actual = position(246)
            esperado = ((7, 4))
            self.assertEqual(actual,esperado)
    def test_position10(self):
            actual = position(74)
            esperado = ((2, 3))
            self.assertEqual(actual,esperado)
    def test_position11(self):
        actual = position(208)
        esperado = ((6, 2))
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
class quoridor_wallstop(unittest.TestCase): 
    def test_wallstop1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "S", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        actual = wallstop(request_data)
        esperado = (1,1,"h")
        self.assertEqual(actual,esperado)
class quoridor_wallstop(unittest.TestCase): 
    def test_wallstop2(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        actual = wallstop(request_data)
        esperado = (7,1,"h")
        self.assertEqual(actual,esperado)
class quoridor_wallstop(unittest.TestCase): 
    def test_wallstop3(self):
        request_data={"event": "your_turn", "data": {"walls": 9.0, "side": "N", "score_2": -50.0, "score_1": -25.0, "board": "  N           N                           N                                                                                                                          -*-                                                                                                          S     S     S  ", "remaining_moves": 190.0, "player_2": "dani.fredrikson@gmail.com", "player_1": "armandogerman@hotmail.com", "turn_token": "65d2a9de-e739-43b3-9006-b13e20328b80", "game_id": "05053532-d7d2-11ec-aef0-7ecdf393f9cc"}}
        actual = wallstop(request_data)
        esperado = (7,1,"h")
        self.assertEqual(actual,esperado)
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
    def test_move2(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "S", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (8,1),(7,1)
        self.assertEqual(actual,esperado)
    def test_move3(self):
        request_data={"event": "your_turn", "data": {"side": "N", "walls": 10.0, "player_2": "armandogerman@hotmail.com", "board": "  N           N                           N                                                                                                                                                                                                                                       S     S     S  ", "score_2": -20.0, "score_1": -8.0, "remaining_moves": 196.0, "player_1": "armandogerman@hotmail.com", "turn_token": "d0266bf0-d4f9-4fef-a985-1c8124372b10", "game_id": "471249b2-d7b7-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (1,4),(2,4)
        self.assertEqual(actual,esperado)
    def test_move4(self):
        request_data={"event": "your_turn", "data": {"walls": 9.0, "remaining_moves": 191.0, "score_1": -25.0, "side": "N", "player_1": "armandogerman@hotmail.com", "board": "  N           N            -*-            N                                                                                                                                                                                                              |                *       S     S  |  S  ", "score_2": -27.0, "player_2": "armandogerman@hotmail.com", "turn_token": "6c1b2853-b6e3-437c-8b36-e8639bae90c8", "game_id": "471249b2-d7b7-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (1,4),(2,4)
        self.assertEqual(actual,esperado)
    def test_move5(self):
        request_data={"event": "your_turn", "data": {"player_1": "martin2005@gmail.com", "walls": 10.0, "remaining_moves": 197.0, "score_2": -10.0, "score_1": 6.0, "board": "        N     N                                                       N                                                                                                                                                                                                           S     S     S  ", "player_2": "armandogerman@hotmail.com", "side": "N", "turn_token": "62a2649b-f050-475f-b591-f1d5e3e5a345", "game_id": "18810ece-d7b9-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (2,1),(3,1)
        self.assertEqual(actual,esperado)
    def test_move6(self):
        request_data={"event": "your_turn", "data": {"board": "  N     N     N                                                                                                                                                                                                                                 S                                       S     S  ", "side": "S", "score_1": -10.0, "score_2": 2.0, "walls": 10.0, "player_1": "armandogerman@hotmail.com", "player_2": "eldalai@gmail.com", "remaining_moves": 198.0, "turn_token": "2a93925a-16d7-4935-9ceb-173f6980068f", "game_id": "195c0e52-d7b9-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (7,1),(6,1)
        self.assertEqual(actual,esperado)
    def test_move7(self):        
        request_data={"event": "your_turn", "data": {"player_1": "martin2005@gmail.com", "side": "N", "score_2": -20.0, "board": "        N     N                                                                                         N                                                                                                                                                                         S     S     S  ", "player_2": "armandogerman@hotmail.com", "score_1": 14.0, "remaining_moves": 195.0, "walls": 10.0, "turn_token": "2cc06d18-d455-4993-b617-f74472ff38a5", "game_id": "18810ece-d7b9-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (3,1),(4,1)
        self.assertEqual(actual,esperado)
    def test_move8(self):
        request_data={"event": "your_turn", "data": {"player_1": "armandogerman@hotmail.com", "score_1": -28.0, "walls": 10.0, "side": "S", "score_2": 30.0, "board": "  N           N                           N                                                                                                           S                                                                                                                           S     S        ", "remaining_moves": 192.0, "player_2": "lucas.a.cardone@gmail.com", "turn_token": "dd4c5f30-1728-422b-8590-6b30d9ac4dd7", "game_id": "217c0f10-d7b9-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (4,7),(3,7)
        self.assertEqual(actual,esperado)
    def test_move9(self):
        request_data={"event": "your_turn", "data": {"walls": 9.0, "side": "N", "score_2": -50.0, "score_1": -25.0, "board": "  N           N                           N                                                                                                                          -*-                                                                                                          S     S     S  ", "remaining_moves": 190.0, "player_2": "dani.fredrikson@gmail.com", "player_1": "armandogerman@hotmail.com", "turn_token": "65d2a9de-e739-43b3-9006-b13e20328b80", "game_id": "05053532-d7d2-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (1,4),(2,4)
        self.assertEqual(actual,esperado)
    def test_move10(self):
        request_data={"event": "your_turn", "data": {"remaining_moves": 164.0, "score_1": -19.0, "player_1": "armandogerman@hotmail.com", "score_2": -45.0, "side": "N", "player_2": "armandogerman@hotmail.com", "walls": 7.0, "board": "         N     N                            |         -*- -*-*                | |                *-*-       |     |       -*-*                |   |                *       N       S|       -*- -*-                                                  S           S  ", "turn_token": "ce295c93-6fc0-4477-9852-cb75e878e0ae", "game_id": "53ba8d7e-dafe-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (1,4),(2,4)
        self.assertEqual(actual,esperado)
class quoridor_mindistop(unittest.TestCase): 
    def test_mindistop1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        actual = mindistop(request_data)
        esperado = 274
        self.assertEqual(actual,esperado)
if __name__ == "__main__":
    unittest.main()