def x(profile, element, content):
  if element == "size":
    profile[0] = content
  elif element == "amount":
    profile[1] = content
  elif element == "key":
    profile[2] = content
  else:
    print("ERROR: ELEMENT NOT FOUND")
  if profile == None:
    return(["256x256", 1, "placeholderKey"])
  return(profile)
