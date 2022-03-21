
import random

name = input ("Enter your name? ")
question = input("Enter your 'yes' or 'no' question: ")

#name = "Rick"
#question = "Do I know Python?"
answer = " "
random_number = random.randint(1,11)

# print(random_number)

if random_number == 1 :
  answer = "Yes - definitely."
elif random_number == 2 :
  answer = "It is decidedly so."
elif random_number == 3 :
  answer = "Without a doubt."
elif random_number == 4 :
  answer = "Reply hazy, try again."
elif random_number == 5 :
  answer = "Ask again later."
elif random_number == 6 :
  answer = "Better not tell you now."
elif random_number == 7 :
  answer = "My sources say no."
elif random_number == 8 :
  answer = "Outlook not so good."
elif random_number == 9 :
  answer = "Very doubtful."
elif random_number == 10 :
  answer = "Go for it."
elif random_number == 11 :
  answer = "No go."
else:
  answer = "Error"
if name != " ":
  print("\n" + name + " asks: " + question)
else: print("Question: " + question)
if question != " ":
  print("Magic 8-Ball's answer: " + answer)
else: print("User entry invalid!")