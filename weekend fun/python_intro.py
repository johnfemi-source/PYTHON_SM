message = "Enter a number:"

player1_input = input(message)

player2_input = input(message)

 
if player1_input == player2_input:
   
    print("TIE")

elif player1_input == 'scissor' and player2_input == 'paper' :
   
      print("player1 wins")

elif player2_input == 'scissor' and player1_input == 'paper' :

       print("player2 wins")

elif player1_input == 'rock' and player2_input == 'scissor' :
     
       print("player1 wins")

elif player2_input == "rock" and player1_input == 'scissor' :
     
       print("player2 win")


