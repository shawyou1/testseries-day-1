def appendMiddle(a,b):
   a=(a[:len(a)//2]+b+a[(len(a)//2):])   # function to append in middle
   return a
if __name__ == '__main__':
  a=input()
  b=input()
  a=appendMiddle(a,b)
  print(a)
  
