import matplotlib.pyplot as plt # import plt for graphing
import numpy as np # import numpy to use the array for data
import random # import random to use for rollHandler
def rollHandler(dice): # defines rollHandler with the input variable dice (embeded dieRoll function)
  inputList=[]
  outputList=[]
  for i in dice.split('d'): 
    inputList.append(i)
  for i in range(int(inputList[0])):
    outputList.append(random.randint(1,int(inputList[1])))
  return outputList
def x(dice, file):
  rolledDiceX = rollHandler(dice)
  resultX = np.array(rolledDiceX)
  resultY = random.randint(1,int(dice.split("d")[0]))
  plt.bar(resultX, resultY)
  plt.savefig(file)
  
