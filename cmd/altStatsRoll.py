import random # import random to use for rollHandler
def rollHandler(dice): # defines rollHandler with the input variable dice (embeded dieRoll function)
  inputList=[] # defines the list for data to import to the roller
  outputList=[] # defines the list for the dice rolls to be appended to
  for i in dice.split('d'): # splits the "d" between the dice amount and dice sides
    inputList.append(i) # append the dice amount and sides to a list for rolling
  for i in range(int(inputList[0])): # loops for the amount of dice
    outputList.append(random.randint(1,int(inputList[1]))) # appends the dice rolls to the output list
  return outputList # exports the output list to the main function
def x():
  dice = rollHandler('20d6')
  dice.sort()
  dice.pop(0)
  dice.pop(0)
  rolledDice = []
  rolledDice.append(dice.count(1))
  rolledDice.append(dice.count(2))
  rolledDice.append(dice.count(3))
  rolledDice.append(dice.count(4))
  rolledDice.append(dice.count(5))
  rolledDice.append(dice.count(6))
  return rolledDice
