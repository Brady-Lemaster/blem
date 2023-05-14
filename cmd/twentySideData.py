import random # import random to use for rollHandler
def rollHandler(dice): # defines rollHandler with the input variable dice (embeded dieRoll function)
  inputList=[] # defines the list for data to import to the roller
  outputList=[] # defines the list for the dice rolls to be appended to
  for i in dice.split('d'): # splits the "d" between the dice amount and dice sides
    inputList.append(i) # append the dice amount and sides to a list for rolling
  for i in range(int(inputList[0])): # loops for the amount of dice
    outputList.append(random.randint(1,int(inputList[1]))) # appends the dice rolls to the output list
  return outputList # exports the output list to the main function
def x(number): # defines the function with a parameter for the amount of twenty sided dice
  dice = rollHandler(number+"d20") # rolls the amount of twenty sided dice and adds them to a list
  diceAmount = [] # creates an empty list for appending
  for i in range(20): # loop 20 times
    diceAmount.append(dice.count(i+1)) # appends to the empty list the amount of a certain roll based on the range() function
  return(diceAmount) # return amount of each role
