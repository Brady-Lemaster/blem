def x(file):
  list = []
  with open(file, 'r') as f:
    for line in f.readlines():
      list.append(line.strip())
  return list
