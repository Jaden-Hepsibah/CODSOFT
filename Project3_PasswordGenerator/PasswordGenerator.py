import random
import string

def generate_pass(lengths):
  characters=string.ascii_letters+string.digits+string.punctuation
  password=''.join(random.choices(characters, k=lengths))
  return password
try:
  pass_length=int(input("Enter the desired length of the password: "))
  if pass_length<=0:
    print("Enter a positive number")
  else:
    password=generate_pass(pass_length)
    print("The generated password is:", password)
except ValueError:
  print("Invalid Input. Try Again!")
          

