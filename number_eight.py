def mainFunction(a,b):
  def subFunction(c,d):
    return c+d
  x = subFunction(a,b)
  return x
result = mainFunction(5,10)
print(result)
