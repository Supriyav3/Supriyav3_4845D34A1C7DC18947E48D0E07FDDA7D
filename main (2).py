def fact_rect(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rect(n-1)

n=int(input("enter a number:"))
res=fact_rect(n)

print("The factorial of {} is {}:".format(n,res))
 
