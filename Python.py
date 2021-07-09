from typing import overload


name = input('Hello reader! What is your name?' )
place = input('Where are you from?')
print (f'Hello {name.title()}! It is a pleasure to meet you. I am Deivid!')
if place.capitalize() == 'Brazil':
  print(f'Oh, so you are from {place.capitalize()} too! I wonder if we are going to meet someday!')
else:
  print(f'I want to travel around all the world! Maybe someday I will come to {place}!')
print(f'{name.title()}, thanks for reading this simple code!')