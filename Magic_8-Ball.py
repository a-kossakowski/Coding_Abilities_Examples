#Simple script that aims to imitate famous toy, "Magic 8-Ball".
#Based on some user input it`s suppose to give some important, life changing, advices :)

#Here is a part of code which aims to take some input from the user.
#Variable for user`s name
print ("Hello, it`s the Magic 8-Ball script in Python!")
input ("Press ENTER to continue.")
name = input("What`s Your name?")
input ("Press ENTER to continue.")
#Variable for user`s question
question = input ("What`s Your question?")
input ("Press ENTER to continue.")
#Here i`ve defined empty variable for a coming anserw, just so its easier to manage in code.
answer = ""
import random
#Numbers range from 1 - 9, because 9 isn`t inclusive.
random_number = random.randint (1, 9)
#Here i`ve set answers for each number that was previously generated
if random_number == 1:
  answer = "Yes, definitely"
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  print ("Very doubtful.")
#Here i made a part af code for a user, that desires to test if I consider the opportunity that he wont giv me any inputs : )
if name == "" and question == "":
  print ("Give a name or a question.")
elif name != "" and question == "":
  print (name, "didn`t ask question.")
elif name == "" and question != "":
  print (question, answer)
#Here teh code takes both user inputs, if both were given
else:
  print (name, "asks", question, "The answer from Magic 8-ball is:", answer)
input ("Press ENTER to exit.")
