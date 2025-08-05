import random

def play_game():
        low = int(input("\nEnter Lower Bound: "))
        high = int(input("Enter Higher Bound: "))

        print(f"\nYou have 6 chances to guess the number between {low} and {high}. Let's start it!!  ")
        
        num = random.randint(low,high) #to genrate randome number
        chances = 6 #chance for guess
        guess_count = 0
        
        while guess_count < chances:
          guess_count += 1
          guess = int(input("\nEnter your guess: "))
          
          if guess == num:
            print(f"Congratulations!! The number is {num}. You guessed it in {guess_count} attempts")
            print("Play Again!!")
            break
        
          elif guess_count >= chances and guess != num:
            print(f"Better Luck Next Time!!, The number was {num} and you're out of chances.")
            break
            
          elif guess > num :
            print("Its too high, guess a lower one")
            
          elif guess < num :
            print("Its too low , guess a higher one")
            
          elif guess_count == 1 and guess == num:
              print("You're such a brilliant")


while True:
    frs = input("Hi! Welcome to the Number Guessing Game.\nYou have 6 chances to guess the number. Let's start! (y/n):").lower()
    if frs == "y":
        play_game()
        if frs == "y":
            do = input("wanna play again? (y/n): ")
            if do == "y":
                play_game()
        
    if frs == "n":
        break
