def factorial_1(x):
  f_old = 1
  f = 1

  for i in range(x):
    f = f*f_old
    f_old += 1
    
  return f
