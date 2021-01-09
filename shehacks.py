import random

#The user chooses the numbers for the range 
print("Choose a range of numbers")
start = int(input("Enter first number: "))
end = int(input("Enter last number: "))

#Exit app if user inputs data format 
if(start > end): 
  print("Incorrect range")
  exit()

#generate random number 
random = random.randint(start,end)

#run loop until number is correctly guessed 
while True:
  userguess = (input("Guess random number:"))

  #checks if input number is of type integer
  if (userguess.isdigit() is False):
    print("Error. Only integers are allowed")

  elif (int(userguess) < random):
    print("Incorrect. The number is higher")

  elif (int(userguess) > random):
    print("Incorrect. The number is lower")

  else:
    print("Congratulations. You guessed the number!")
    break




