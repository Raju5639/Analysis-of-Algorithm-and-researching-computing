from random import randrange

def partition(x,pivot_index=0):
   i=0
   if pivot_index !=0: x[0],x[pivot_index] = x [pivot_index],x[0]
   for j in range(len(x)-1):
      if x[j+1]< x[0]:
         x[j+1],x[i+1] = x[i+1],x[j+1]
         i+=1
   x[0],x[i]= x[i],x[0]
   return x,i

def rselect(x,k):
   if len(x)==1:
      return x[0]
   else:
      xpart = partition(x,randrange(len(x)))
      x =xpart[0]
      j =xpart[1]
      if j==k:
         return x[j]

      elif j>k:
         return rselect(x[:j],k)
      else:
         k=k-j-1
         return rselect(x[(j+1):],k)
x=[3,1,8,2,12,55]
for i in range(len(x)):
   print(rselect(x,i))
      
