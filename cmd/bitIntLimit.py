def x(bits):
  bitMax=0
  bitNumber=[]
  for i in range(bits):
    bitNumber.append(2**i)
  for i in range(len(bitNumber)):
    bitMax=bitMax+bitNumber[i]
  return bitMax
