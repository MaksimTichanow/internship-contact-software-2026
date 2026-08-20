import os
import random
import subprocess
from mt import clear

# Variablen
s1_win = False
s2_win = False
s1_sign = ""
s2_sign = ""
s1_turn = False
s2_turn = False
s1_name = ""
s2_name = ""
rounds_played = 0
draw = False


# Listen
spielfeld = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
    ]


# Funktionen


def spielfeld_output():

    global spielfeld

    for zeile in spielfeld:
        print(zeile)



def spieler_namen():

    global s1_name
    global s2_name
    global s1_turn
    global s2_turn
    global s1_sign
    global s2_sign


    s1_name = input("Spieler 1 Name: ")
    s2_name = input("Spieler 2 Name: ")
    s1_sign = input(f"{s1_name} Zeichen: ")
    s2_sign = input(f"{s2_name} Zeichen: ")

    # Zeichen Check
    if s1_sign not in ("X", "O"):
        print("Invalid Sign! Returning to Player Names!")
        spieler_namen()
    if s2_sign not in ("X", "O"):
        print("Invalid Sign! Returning to Player Names!")
        spieler_namen()

    # Start Spieler Check

    if s1_sign == "X":
        print(f"{s1_name} beginnt.\n")
        s1_turn = True
        s2_turn = False
    else:
        print(f"{s2_name} beginnt.\n")
        s2_turn = True
        s1_turn = False

    spielfeld_output()
    spieler_inputs()


def spieler_inputs():
    global s1_turn
    global s2_turn
    global spielfeld
    global rounds_played
    global s1_win
    global s2_win


    if s1_win == True or s2_win == True:
        input("Press any key to exit...")
        return

    # Zug Check
    if s1_turn == True:
        print(f"{s1_name} ist dran!")  
        print(f"Runden gespielt: {rounds_played}")      
        z = int(input("Zeile: "))
        s = int(input("Spalte: "))
        spielfeld[z][s] = s1_sign
        spielfeld_output()
        rounds_played += 1  
        s1_turn = False
        s2_turn = True
        win_check()
        

    if s2_turn == True:
        print(f"{s2_name} ist dran!")
        print(f"Runden gespielt: {rounds_played}")
        z = int(input("Zeile: "))
        s = int(input("Spalte: "))
        spielfeld[z][s] = s2_sign
        spielfeld_output()
        rounds_played += 1  
        s1_turn = True
        s2_turn = False
        win_check()

                    

def win_check():
    global spielfeld
    global s1_name
    global s2_name
    global s1_sign
    global s2_sign
    global s1_win
    global s2_win

    # Horizontal

    if spielfeld[0][0] =='X' and spielfeld[0][1] == 'X' and spielfeld[0][2] == 'X':
        if s1_sign == 'X':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
        else:
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True

    elif spielfeld[1][0] == 'X' and spielfeld[1][1] == 'X' and spielfeld[1][2] == 'X':
        if s1_sign == 'X':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
        else:
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True

    elif spielfeld[2][0] == 'X' and spielfeld[2][1] == 'X' and spielfeld[2][2] == 'X':
        if s1_sign == 'X':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
        else: 
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True

    # Vertikal

    elif spielfeld[0][0] == 'X' and spielfeld[1][0] == 'X' and spielfeld[2][0] == 'X':
        if s1_sign == 'X':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
        else: 
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True

    elif spielfeld[0][1] == 'X' and spielfeld[1][1] == 'X' and spielfeld[2][1] == 'X':
        if s1_sign == 'X':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
        else:
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True

    elif spielfeld[0][2] == 'X' and spielfeld[1][2] == 'X' and spielfeld[2][2] == 'X':
        if s1_sign == 'X':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
        else:
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True

    # Schräg

    elif spielfeld[0][0] == 'X' and spielfeld[1][1] == 'X' and spielfeld[2][2] == 'X':
        if s1_sign == 'X':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
        else:
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True

    elif spielfeld[0][2] == 'X' and spielfeld[1][1] == 'X' and spielfeld[2][0] == 'X':
        if s1_sign == 'X':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
        else: 
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True


    # Kreis


    # Horizontal

    if spielfeld[0][0] =='O' and spielfeld[0][1] == 'O' and spielfeld[0][2] == 'O':
        if s1_sign == 'O':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
            
        else:
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True
            

    elif spielfeld[1][0] == 'O' and spielfeld[1][1] == 'O' and spielfeld[1][2] == 'O':
        if s1_sign == 'O':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
        else:
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True            
    
    elif spielfeld[2][0] == 'O' and spielfeld[2][1] == 'O' and spielfeld[2][2] == 'O':
        if s1_sign == 'O':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
        else: 
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True

    # Vertikal


    elif spielfeld[0][0] == 'O' and spielfeld[1][0] == 'O' and spielfeld[2][0] == 'O':
        if s1_sign == 'O':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
        else: 
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True

    elif spielfeld[0][1] == 'O' and spielfeld[1][1] == 'O' and spielfeld[2][1] == 'O':
        if s1_sign == 'O':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
        else:
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True

    elif spielfeld[0][2] == 'O' and spielfeld[1][2] == 'O' and spielfeld[2][2] == 'O':
        if s1_sign == 'O':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
        else:
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True

    # Schräg

    elif spielfeld[0][0] == 'O' and spielfeld[1][1] == 'O' and spielfeld[2][2] == 'O':
        if s1_sign == 'O':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
        else:
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True

    elif spielfeld[0][2] == 'O' and spielfeld[1][1] == 'O' and spielfeld[2][0] == 'O':
        if s1_sign == 'O':
            print(f"{s1_name} hat das Spiel gewonnen!")
            s1_win = True
        else: 
            print(f"{s2_name} hat das Spiel gewonnen!")
            s2_win = True

    if rounds_played > 5: 
        print("Unentschieden")
        input()
    
