import matplotlib.pyplot as plt # import plt for graphing
import numpy as np # import numpy to use the array for data
import random # import random to use for rollHandler
def rollHandler(dice): # defines rollHandler with the input variable dice (embeded dieRoll function)
  inputList=[] # defines the list for data to import to the roller
  outputList=[] # defines the list for the dice rolls to be appended to
  for i in dice.split('d'): # splits the "d" between the dice amount and dice sides
    inputList.append(i) # append the dice amount and sides to a list for rolling
  for i in range(int(inputList[0])): # loops for the amount of dice
    outputList.append(random.randint(1,int(inputList[1]))) # appends the dice rolls to the output list
  return outputList # exports the output list to the main function
def x(dice, file): # defines the main function with the rolled dice and the export file
  rolledDiceX = rollHandler(dice) # rolls dice for the data to add to the graph
  resultX = np.array(rolledDiceX) # converts rhe data to a numpy array
  resultY = random.randint(1,int(dice.split("d")[0])) # randomly picks between the amount of dice rolled and 1 for graph
  plt.bar(resultX, resultY) # adds the data (resultX) and the amount of rolls in a section (resultY)
  plt.savefig(file) # saves to the designated file
  
