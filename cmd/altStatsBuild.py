def statsBuild(rolledDice, die1, die2, die3): # define the function with a rolled set of dice and the dice to use as inputs
  if rolledDice[die1-1] > 0 and rolledDice[die2-1] > 0 and rolledDice[die3-1] > 0: # checks if theres enough dice
    rolledDice[die1-1] = rolledDice[die1-1]-1 # if so subtracts the first die from the dataset
    rolledDice[die2-1] = rolledDice[die2-1]-1 # then the second
    rolledDice[die3-1] = rolledDice[die3-1]-1 # and then the third
    stat = die1 + die2 + die3 # adds the dice for the stat
    return(rolledDice, stat) # returns the changed dataset along with the stat value
  else: # if there arent enough dice
    return(rolledDice, "error") # if no returns the unchanged dataset and "error"
