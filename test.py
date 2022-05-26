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
    def test_position12(self):
        actual = position(16)
        esperado = ((0, 8))
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
    def test_wallstop2(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        actual = wallstop(request_data)
        esperado = (7,1,"h")
        self.assertEqual(actual,esperado)
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
        request_data={"event": "your_turn", "data": {"side": "S", "score_1": 1508.0, "walls": 10.0, "board": "        N     N                           S                                                                                                                                                                                                     N                                         S   S  ", "player_2": "armandogerman@hotmail.com", "remaining_moves": 170.0, "player_1": "armandogerman@hotmail.com", "score_2": 1482.0, "turn_token": "1a432ad0-fdd2-4a36-823b-5481b18428af", "game_id": "6ff9cf22-dc20-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (1,4),(0,3)
        self.assertEqual(actual,esperado)
    def test_move11(self):
        request_data={"event": "your_turn", "data": {"board": "            N N                               S                                                                                                                                                               N                                                                               S S", "score_1": 3870.0, "side": "S", "remaining_moves": 141.0, "player_2": "armandogerman@hotmail.com", "player_1": "armandogerman@hotmail.com", "walls": 10.0, "score_2": 3998.0, "turn_token": "b196b770-1986-401f-8b62-ceb73d5370b7", "game_id": "9a48fc0e-dc29-11ec-aef0-7ecdf393f9cc"}}        
        actual = move(request_data)
        esperado = (1,6),(0,5)
        self.assertEqual(actual,esperado)
    def test_move12(self):
        request_data={"event": "your_turn", "data": {"side": "N", "player_1": "armandogerman@hotmail.com", "remaining_moves": 170.0, "player_2": "armandogerman@hotmail.com", "board": "              N N                                                                                                                                                                                                                                     N                           S     S     S  ", "score_2": 2492.0, "walls": 10.0, "score_1": 1508.0, "turn_token": "27aac30f-518e-452e-8e0a-b31b21f28dd7", "game_id": "6254d0f4-dc3b-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (7,4),(8,5)
        self.assertEqual(actual,esperado)
    def test_move13(self): #tendria que saltar la S. despues se queda encerrado.
        request_data={"event": "your_turn", "data": {"side": "N", "score_2": 5517.0, "board": "  N N              -*-              S                      -*-          S     S N                -*-                                                           -*-                                                                                                 -*-                           ", "player_1": "armandogerman@hotmail.com", "score_1": 8654.0, "walls": 10.0, "player_2": "mamerida2013@gmail.com", "remaining_moves": 66.0, "turn_token": "166bc6a3-8982-414c-ae97-51d2d9b742f8", "game_id": "5243783e-dc43-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (2,6),(2,7)
        self.assertEqual(actual,esperado)
    def test_move14(self): #ponen una pared y se va a la izquierda. ahi muere (pawns4) pawnmoveleft S ((4, 0), None)
        request_data={"event": "your_turn", "data": {"board": "  N     N                                                                                                              -*-                S           N                                                                                                                                 S     S  ", "walls": 10.0, "player_1": "matiasbertani@gmail.com", "player_2": "armandogerman@hotmail.com", "score_2": 30.0, "remaining_moves": 191.0, "score_1": 33.0, "side": "S", "turn_token": "db1526f4-66f3-4928-a97f-2b7ab06b7465", "game_id": "e9fa3fc4-dc4c-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (4,1),(4,2)
        self.assertEqual(actual,esperado)
    def test_move15(self): #No salta para ganar pawnmovedown N ((7, 1), (8, 2))
        request_data={"event": "your_turn", "data": {"side": "N", "player_1": "armandogerman@hotmail.com", "walls": 10.0, "score_1": 254.0, "board": "        N     N                                 S                                                                                                                                                                                               N                                 S     S        ", "score_2": 254.0, "remaining_moves": 186.0, "player_2": "nahuel9567@gmail.com", "turn_token": "5c15d2cc-f161-40e5-b186-38636c4fd680", "game_id": "87a4d4f2-dc50-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (7,1),(8,2)
        self.assertEqual(actual,esperado)
    def test_move16(self): #esta encerrado. sube uno y despues se cuelga. deberia arrancar otro peon. pawns4
        request_data={"event": "your_turn", "data": {"side": "N", "score_2": 10325.0, "player_2": "pablogg011@gmail.com", "score_1": 3242.0, "remaining_moves": 16.0, "board": "        N     N                             S                                                          |N|              * *              | |             -*-                                                                                                                                S S  ", "player_1": "armandogerman@hotmail.com", "walls": 10.0, "turn_token": "40447da0-5225-4096-a524-774532bbb0fd", "game_id": "9a7b043e-dc55-11ec-aef0-7ecdf393f9cc"}}
        actual = move(request_data)
        esperado = (0,4),(1,4)
        self.assertEqual(actual,esperado)

        
class quoridor_mindistop(unittest.TestCase): 
    def test_mindistop1(self):
        request_data={"event": "your_turn", "data": {"walls": 10.0, "score_1": 0.0, "remaining_moves": 200.0, "player_1": "armandogerman@hotmail.com", "side": "N", "score_2": 0.0, "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ", "player_2": "armandogerman@hotmail.com", "turn_token": "59ac08e3-bdf9-4787-82ed-b9b49b304a9e", "game_id": "eb6b710a-d695-11ec-aef0-7ecdf393f9cc"}}
        actual = mindistop(request_data)
        esperado = 274
        self.assertEqual(actual,esperado)
if __name__ == "__main__":
    unittest.main()