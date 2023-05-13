def x(profile, element, content):
  if element == "model":
    profile[0] = content
  elif element == "random":
    profile[1] = content
  elif element == "limit":
    profile[2] = content
  elif element == "key":
    profile[3] = content
  else:
    print("ERROR: ELEMENT NOT FOUND")
  if profile == None:
    return(["ada", 50, "placeholderKey"])
  return(profile)
 
