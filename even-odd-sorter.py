print("Welcome to Even Odd Number Sorter App")

state = True

#Run the program as long as the user wants
while state:
  #Get user input
  num_string = input(f"Enter a string of numbers separated by a comma (,): ")
  #Delete empty spaces if any
  num_string = num_string.replace(" ", "")
  num_list = num_string.split(",")

  # Initialize lists to hold even and odd values
  evens = []
  odds = []
  
  print(f"\n----- Result Summary -----")  
  for each in num_list:
    each = int(each)
    if each % 2 == 0:
      evens.append(each)
      print(f"\t{each} is even!")
    else:
      odds.append(each)
      print(f"\t{each} is odd!")

  #Sort the lists
  evens.sort()
  odds.sort()

  #Show even numbers in numerical order
  print(f"\nThe following {len(evens)} numbers are even:")
  for even in evens:
    print(f"\t{even}")

  #Show odd numbers in numerical order
  print(f"\nThe following {len(odds)} numbers are odd:")
  for odd in odds:
    print(f"\t{odd}")

  choice = input(f"\nWould you like to run the program again (y/n): ")
  if choice != "y":
    state = False

print(f"\nThank you for using the program. Goodbye!")