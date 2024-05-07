## works

def front_back(str):
  if len(str) < 2:
    return str
  else:
    front = str[0:1]
    back = str[len(str)-1]
  return back+str[1:len(str)-1]+front
