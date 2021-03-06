from .ChessPiece import ChessPiece, find_chess_piece
from .Color import Color

class Rook(ChessPiece):
  def __init__(self,x,y,color):
    super().__init__(x,y,color)

  def __str__(self):
      if (self.color == Color.BLACK):
          return "r"
      else:
          return "R"

  def __check_north(self, chess_pieces):
    for y in range(self.y+1,8):
      x = self.x

      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return None, chess_piece
        else:
          return chess_piece, None

    return None,None

  def __check_east(self, chess_pieces):
    for x in range(self.x+1,8):
      y = self.y

      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return None, chess_piece
        else:
          return chess_piece, None

    return None,None

  def __check_south(self, chess_pieces):
    for y in range(self.y-1,-1,-1):
      x = self.x

      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return None, chess_piece
        else:
          return chess_piece, None

    return None,None

  def __check_west(self, chess_pieces):
    for x in range(self.x-1,-1,-1):
      y = self.y

      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return None, chess_piece
        else:
          return chess_piece, None

    return None,None

  def __check_rook(self,chess_pieces):
    attacked_ally = []
    attacked_ally.append(self.__check_north(chess_pieces)[0]) if self.__check_north(chess_pieces)[0] != None else None
    attacked_ally.append(self.__check_east(chess_pieces)[0]) if self.__check_east(chess_pieces)[0] != None else None
    attacked_ally.append(self.__check_south(chess_pieces)[0]) if self.__check_south(chess_pieces)[0] != None else None
    attacked_ally.append(self.__check_west(chess_pieces)[0]) if self.__check_west(chess_pieces)[0] != None else None

    attacked_enemy = []
    attacked_enemy.append(self.__check_north(chess_pieces)[1]) if self.__check_north(chess_pieces)[1] != None else None
    attacked_enemy.append(self.__check_east(chess_pieces)[1]) if self.__check_east(chess_pieces)[1] != None else None
    attacked_enemy.append(self.__check_south(chess_pieces)[1]) if self.__check_south(chess_pieces)[1] != None else None
    attacked_enemy.append(self.__check_west(chess_pieces)[1]) if self.__check_west(chess_pieces)[1] != None else None

    return attacked_ally, attacked_enemy

  def list_attacked_ally(self,chess_pieces):
    return self.__check_rook(chess_pieces)[0]

  def list_attacked_enemy(self,chess_pieces):
    return self.__check_rook(chess_pieces)[1]
