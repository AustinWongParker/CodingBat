def missing_char(str, n):
  
  # if the index is not target (n), then add it to new string
  
  # if it is the target, do not add it
  new_string = ''
  
  for count, char in enumerate(str):
    if count != n:
      new_string+=str[count]
    elif count == n:
      pass
      
    return new_string
    
    ## It is saying my solution is not correct, but it works in python interactive
    ## It's more involved with a for loop, so the string splicing is prob better