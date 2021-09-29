import random

name = 'John Doe'
question = 'If I could, should I?'
answer = ''

random_number = random.randint(1,9)

#Default value of name
if name == '':
  name = 'Stranger'

#Default value of question
if question == '':
  question = 'What would you like to know?'
else:
  question = question

#8-Ball Answers"
if random_number == 1:
  answer = 'Yes - definitely.'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt.'
elif random_number == 4:
  answer = 'Reply hazy, try again.'
elif random_number == 5:
  answer = 'Ask again later.'
elif random_number == 6:
  answer = 'Better not tell you now.'
elif random_number == 7:
  answer = 'My sources say no.'
elif random_number == 8:
  answer = 'Outlook not so good.'
elif random_number == 9:
  answer = 'Very doubtful.'
else: 
  answer = 'Error'

print(name + ' asks: '+ question)
print("Magic 8-Ball's answer: " + answer)

#Disclaimer:
#Please don't use the program to make irrational decisions. You're awesome!
