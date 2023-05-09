import matplotlib.pyplot as plt
import numpy as np
import random
def rollHandler(dice):
  inputList=[]
  outputList=[]
  for i in dice.split('d'): 
    inputList.append(i)
  for i in range(int(inputList[0])):
    outputList.append(random.randint(1,int(inputList[1])))
  return outputList
def x(dice, file):
  rolledDiceX = blem.dieRoll.x(dice)
  resultX = np.array(rolledDiceX)
  resultY = random.randint(1,int(dice.split("d")[0]))
  plt.bar(resultX, resultY)
  plt.savefig(file)
  
