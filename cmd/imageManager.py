def x(profile, element, content):
  if profile == None:
    profile = ["256x256", 1, "placeholderKey"]
  if element == "size":
    profile[0] = content
  elif element == "amount":
    profile[1] = content
  elif element == "key":
    profile[2] = content
  else:
    print("ERROR: ELEMENT NOT FOUND")
  return(profile)
