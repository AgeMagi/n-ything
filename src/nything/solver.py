from .fitness import *
from random import randint
import copy
from model import find_chess_piece  

def more_optimal(min_same_color_attacks, max_different_color_attacks, current_chess_pieces):
    (same_color_attacks, different_color_attacks) = fitness(current_chess_pieces)

    if ((max_different_color_attacks - min_same_color_attacks) < (different_color_attacks - same_color_attacks)):
        return True
    elif ((max_different_color_attacks - min_same_color_attacks) == (different_color_attacks - same_color_attacks)):
        if (same_color_attacks <= min_same_color_attacks):
            return True

    return False

def random_position(chess_pieces):
    (random_x, random_y) = (randint(0, 7), randint(0, 7))

    while(None != find_chess_piece(chess_pieces, random_x, random_y)):
        (random_x, random_y) = (randint(0, 7), randint(0, 7))

    return (random_x, random_y)

def generate_move(chess_pieces):
    current_chess_pieces = copy.deepcopy(chess_pieces)
    (min_same_color_attacks, max_different_color_attacks) = fitness(chess_pieces)

    for k in range(0, len(chess_pieces)):
        current_x = current_chess_pieces[k].x
        current_y = current_chess_pieces[k].y
        
        for i in range(0, 8):
            for j in range(0, 8):
                if (find_chess_piece(chess_pieces, i, j) == None):
                    current_chess_pieces[k].x = i
                    current_chess_pieces[k].y = j
                    
                    (same_color_attacks, different_color_attacks) = fitness(current_chess_pieces)
                    
                    if (more_optimal(min_same_color_attacks, max_different_color_attacks, current_chess_pieces)):
                        
                        min_same_color_attacks = same_color_attacks
                        max_different_color_attacks = different_color_attacks
                        
                        for l in range(len(chess_pieces)):
                            chess_pieces[l].x = current_chess_pieces[l].x
                            chess_pieces[l].y = current_chess_pieces[l].y

                    current_chess_pieces[k].x = current_x
                    current_chess_pieces[k].y = current_y

    return

def generate_move_random(chess_pieces):
    random_chess_pieces = copy.deepcopy(chess_pieces)

    random_bidak = randint(0, len(random_chess_pieces)-1)

    (random_x, random_y) = random_position(random_chess_pieces)
    
    random_chess_pieces[random_bidak].x = random_x
    random_chess_pieces[random_bidak].y = random_y
    
    return random_chess_pieces

def generate_random_solution(chess_pieces):
    for k in range(0, len(chess_pieces)):
        (random_x, random_y) = random_position(chess_pieces)

        chess_pieces[k].x = random_x
        chess_pieces[k].y = random_y
    
    return chess_pieces