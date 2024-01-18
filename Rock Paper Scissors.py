player1 = input("rock, paper, scissors shoot! (rock, paper, scissors): ")
player2 = input("rock, paper, scissors shoot! (rock, paper, scissors): ")

if player1 == player2:
    print("tie")
if player1 == "rock" and player2 == "scissors":
    print("Rock smashes scissors, player 1 wins!")
if player1 == "scissors" and player2 == "rock":
    print("Rock smashes scissors, player 2 wins!")
if player1 == "scissors" and player2 == "paper":
    print("Scissors cut paper, player 1 wins!")
if player1 == "paper" and player2 == "scissors":
    print("Scissors cut paper, player 2 wins!")
if player1 == "paper" and player2 == "rock":
    print("Paper covers rock, player 1 wins!")
if player1 == "rock" and player2 == "paper":
    print("Paper covers rock, player 2 wins!")


    
