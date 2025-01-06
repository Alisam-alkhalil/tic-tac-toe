def print_board(tic, tac):
   """
    Prints the current state of the tic-tac-toe board and a reference board.
    
    The function takes two lists as input. The first list `tic` represents the current 
    state of the tic-tac-toe board, and the second list `tac` serves as a reference 
    for the player, showing the numbers 1 to 9 corresponding to each position on the board.
    
    Args:
        tic (list): A list of 9 strings representing the current board state, 
                    with each position containing 'X', 'O', or ' '.
        tac (list): A list of 9 integers (1 to 9) representing the positions on the board.
   """

   print("\n")
   print(f"{tic[0]} | {tic[1]} | {tic[2]}")
   print("--+---+--")
   print(f"{tic[3]} | {tic[4]} | {tic[5]}")
   print("--+---+--")
   print(f"{tic[6]} | {tic[7]} | {tic[8]}")
   print("\n")
   print("To choose your place enter a number between 1 and 9 as represented below:\n")
   print(f"{tac[0]} | {tac[1]} | {tac[2]}")
   print("--+---+--")
   print(f"{tac[3]} | {tac[4]} | {tac[5]}")
   print("--+---+--")
   print(f"{tac[6]} | {tac[7]} | {tac[8]}")
   print("\n")

def play(tic, player):
   """
    Prompts the current player to make a move on the tic-tac-toe board.

    The function repeatedly asks the player to enter a move until a valid move
    is provided. A valid move is one where the chosen position on the board is
    not already occupied by 'X' or 'O'. The player's symbol is then placed on
    the board at the chosen position.

    Args:
        tic (list): A list of 9 strings representing the current board state,
                    with each position containing 'X', 'O', or ' '.
        player (str): A string representing the current player, either 'X' or 'O'.

    Returns:
        list: The updated board state with the player's move applied.
    """

   while True:  # Fixed indentation here
      move = input("Enter your move: ")
      index = int(move) - 1
      if tic[index] == "X" or tic[index] == "O":
         print("Invalid move")
      else:
         break
   tic[index] = player
   return tic


def check_win(tic):

   """
    Checks the current state of the tic-tac-toe board for a win condition.

    This function examines the board to determine if either player 'X' or 'O'
    has achieved a winning combination. If a win is detected, it prints the 
    current board state and announces the winner, then exits the program.

    Args:
        tic (list): A list of 9 strings representing the current board state,
                    with each position containing 'X', 'O', or ' '.
    """

   win_conditions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

   for x in win_conditions:
      if tic[x[0]-1] == tic[x[1]-1]  == tic[x[2]-1] == "X" or \
         tic[x[0]-1] == tic[x[1]-1]  == tic[x[2]-1] == "O":
         print("\n")
         print(f"{tic[0]} | {tic[1]} | {tic[2]}")
         print("--+---+--")
         print(f"{tic[3]} | {tic[4]} | {tic[5]}")
         print("--+---+--")
         print(f"{tic[6]} | {tic[7]} | {tic[8]}")
         print("\n")
         print(f"Player {tic[x[0]-1]} wins!")
         exit()
   
   if " " not in tic:
      print("\n")
      print(f"{tic[0]} | {tic[1]} | {tic[2]}")
      print("--+---+--")
      print(f"{tic[3]} | {tic[4]} | {tic[5]}")
      print("--+---+--")
      print(f"{tic[6]} | {tic[7]} | {tic[8]}")
      print("\n")
      print("Draw!")
      exit()
         
def main():

   """
    The main entry point of the program. Initializes the board, the list of players, and the round number, then enters an infinite loop where the current player is prompted to make a move, the board is updated, and the win condition is checked until a player has won.
    """
   tic = [" "] * 9 
   tac = [1,2,3,4,5,6,7,8,9]
   players = ["X", "O"]
   round = 0

   while True:

      print_board(tic, tac)
      print(f"{players[round%2]}'s turn")
      tic = play(tic, players[round%2])
      check_win(tic)
      round +=1

   
if __name__ == "__main__":
   main()
