#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  moves = [['rock'], ['paper'], ['scissors']]
  movesPoss = []

  def recurse(movesLeft, output): #recursive function
    if movesLeft == 0: #once it runs out of moves left, append it to the movesPoss array
      return movesPoss.append(output)
    
    for i in range(0, len(moves)): #looping through all the moves
     recurse(movesLeft -1 , output +  moves[i]) #call function and decrement down the move(times) it has left, concat the out to the move at that position
  
  recurse(n, []) # starting point for the recurse function
  
  return movesPoss


print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')