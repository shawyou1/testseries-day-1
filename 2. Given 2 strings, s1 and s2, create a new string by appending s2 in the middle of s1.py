def appendMiddle(a,b):
  print (a[:len(a)//2]+b+a[(len(a)//2)+1:])   # function to append in middle
  
if __name__ == '__main__':
  a=input()
  b=input()
  appendMiddle(a,b)
  
