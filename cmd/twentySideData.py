import random # import random to use for rollHandler
def rollHandler(dice): # defines rollHandler with the input variable dice (embeded dieRoll function)
  inputList=[] # defines the list for data to import to the roller
  outputList=[] # defines the list for the dice rolls to be appended to
  for i in dice.split('d'): # splits the "d" between the dice amount and dice sides
    inputList.append(i) # append the dice amount and sides to a list for rolling
  for i in range(int(inputList[0])): # loops for the amount of dice
    outputList.append(random.randint(1,int(inputList[1]))) # appends the dice rolls to the output list
  return outputList # exports the output list to the main function
def x(number):
  dice = rollHandler(number+"d20")
  diceAmount = []
  diceAmount.append(dice.count(1))
  diceAmount.append(dice.count(2))
  diceAmount.append(dice.count(3))
  diceAmount.append(dice.count(4))
  diceAmount.append(dice.count(5))
  diceAmount.append(dice.count(6))
  diceAmount.append(dice.count(7))
  diceAmount.append(dice.count(8))
  diceAmount.append(dice.count(9))
  diceAmount.append(dice.count(10))
  diceAmount.append(dice.count(11))
  diceAmount.append(dice.count(12))
  diceAmount.append(dice.count(13))
  diceAmount.append(dice.count(14))
  diceAmount.append(dice.count(15))
  diceAmount.append(dice.count(16))
  diceAmount.append(dice.count(17))
  diceAmount.append(dice.count(18))
  diceAmount.append(dice.count(19))
  diceAmount.append(dice.count(20))
  return(diceAmount)
