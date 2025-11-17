while True:

   number = int( input('enter a valid number '))
   if number > 0:
      print("number is positive")

   elif number < 0:
      print("number is negative")

   else:
      print("number is zero")

   question = input('do you want to exit: ').lower()
   if question == 'exit':
      print('Aurevoir!')
      break
  