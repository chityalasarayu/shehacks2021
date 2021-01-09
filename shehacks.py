import random

print("Choose a range of numbers")
start = int(input("Enter first number: "))
end = int(input("Enter last number: "))

if(start > end): 
  print("Incorrect range")
  exit()

random = random.randint(start,end)

while True:
  userguess = (input("Guess random number:"))

  if (userguess.isdigit() is False):
    print("Error. Only integers are allowed")

  elif (int(userguess) < random):
    print("Incorrect. The number is higher")

  elif (int(userguess) > random):
    print("Incorrect. The number is lower")

  else:
    print("Congratulations. You guessed the number!")
    break




