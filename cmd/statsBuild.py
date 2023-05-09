def statsBuild(rolledDice, die1, die2, die3):
  if rolledDice[die1-1] > 0:
    rolledDice[die1-1] = rolledDice[die1-1]-1
    stat = die1 + die2 + die3
    return(rolledDice, stat)
  else:
    return(rolledDice, "error") 
