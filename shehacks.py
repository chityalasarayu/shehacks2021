import random
print("GUESS RANDOM NUMBER")
while True:#to restart program if requested
  
  #The user chooses the numbers for the range 
  print()
  print("Choose a range of numbers")
  
  #run loop until user inputs valid range
  while True:
    start = int(input("Enter minimum: "))
    end = int(input("Enter maximum: "))
    print()
    
    if(start >= end): 
      print("Minimum should be lower than the maximum. Try again!")
      print()
    else:
      #generate random number 
      value = random.randint(start,end)
      
      #run loop until number is correctly guessed 
      while True:
        userguess = (input("Guess the selected number: "))
        print()
        
        #checks if input number is of type integer
        if (userguess.isdigit() is False):
          print("Error. Only integers are allowed")

        elif (int(userguess) < value):
          print("Incorrect. The number is higher")

        elif (int(userguess) > value):
          print("Incorrect. The number is lower")

        else:
          print("Congratulations. You guessed the number!")

          break
      break
   
  #prompts to run program again
  while True:
    answer = str(input('Run again? (Yes/No): '))
    if answer in ('Yes', 'No'):
      break
    print("Invalid answer.")

  if answer == 'Yes':
    continue
  else:
    print()
    print("Goodbye")
    break


