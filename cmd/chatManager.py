def x(profile, element, content): # the function with an option for the profile list, element to change, and content to add
  if profile == None: # if there isnt a profile to use
    profile = ["ada", 1, 1000, "placeholderKey"] # uses a prebuilt for these purposes
  if element == "model": # checks for element model
    profile[0] = content # changes the model element to content
  elif element == "random": # checks for element random
    profile[1] = content # changes the random element to content
  elif element == "limit": # checks for element limit
    profile[2] = content # changes the limit element to content
  elif element == "key": # checks for element key
    profile[3] = content # changes the key element to content
  else: # if theres no element of the name
    print("ERROR: ELEMENT NOT FOUND") # prints an error
  return(profile) # returns the modified profile
 
