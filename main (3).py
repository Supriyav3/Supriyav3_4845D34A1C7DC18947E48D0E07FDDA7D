def leapyear(year):
  if (year/4==0and year/100!=0):
    return True
  elif  year/400==0:
    return True
  else:
    return False
    
year=int(input("enter a year:"))
res=leapyear(year)
if True:
  print ("this year is leap year")
else:
  print ("this year is not a leap year")
  