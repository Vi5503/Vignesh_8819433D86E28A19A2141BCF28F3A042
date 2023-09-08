#1.1 Implement a recursive function to calculate the factorial of a given number.


def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rec(n - 1)


number = int(input("Enter the value:"))
res = fact_rec(number)

print("The factorial of {} is {}".# Leap year
def isleapyear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False


year = int(input("Enter a year : "))
if isleapyear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))(number, res))