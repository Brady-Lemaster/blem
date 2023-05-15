def x(list, file):
  with open(file, "w") as f:
    for i in range(len(list)):
      f.write(str(list[i]) + "\n")
