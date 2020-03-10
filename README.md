# Quiz 6.1 Answers
Some coding parts of Quiz 6.1

```python
def numberEight():
  def mainFunction(a,b):
    def subFunction(c,d):
      return c+d
    x = subFunction(a,b)
    return x
  result = mainFunction(5,10)
  print(result)

def numberNine():
  x = 0
  a = 0
  b = -5
  if (a>0):
    if(b<0):
      x = x +5
    else:
      x = x +3
  else:
    x = x + 2
  print(x)

def larger(x,y):
  if x != y:
    if x>y:
      print(x)
      print(str(x)+" is larger than "+str(y))
    else:
      print(y)
      print(str(y)+" is larger than "+str(x))  
  else:
    print("These two numbers are equal to each other")

def factorial_1(x):
  f_old = 1
  f = 1

  for i in range(x):
    f = f*f_old
    f_old += 1

  return f

def factorial_2(x):
  f = 1
  for i in range(1,x+1):
    f = f * i
  return f

numberEight()
numberNine()
larger(5,5)
larger(4,9)
larger(85,81)
print(factorial_1(10))
print(factorial_2(10))
```

The output of this is as follows:

```
15
2
These two numbers are equal to each other
9
9 is larger than 4
85
85 is larger than 81
3628800
3628800
```
