# Making a function to say : 'hello'.

## first using 'print'.

print('hello')

## maybe create a function to print any word that you want.

def say_hello(arg):
  if isinstance(arg, str):
    return arg
  else:
    print("{0} must be a type str only".format(arg))
