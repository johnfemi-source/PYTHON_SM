number_of_integer = int(input("Enter number of integers:"))
 
counter = 1
sum_odd = 0
sum_even = 0

while(counter <= number_of_integers):
  
      print("Enter a number")
  
      number = int(input())

      if(number % 2 == 0):
      
          sum_even = number + sum_even

      else:

          sum_odd = number + sum_odd
    
      counter = counter + 1

print("the sum of even numbers and sum of odd number are", sum_even,"and", sum_odd< "respectively")
