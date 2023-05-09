import matplotlib.pyplot as plt
import numpy as np
def x(dice, file):
  rolledDiceX = blem.dieRoll.x(dice)
  rolledDiceY = blem.dieRoll.x(dice)
  numpyDiceX = np.array(rolledDiceX)
  numpyDiceY = np.array(rolledDiceY)
  plt.bar(numpyDiceX, numpyDiceY)
  plt.savefig(file)
