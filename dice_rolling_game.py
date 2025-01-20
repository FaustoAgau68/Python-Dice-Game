import random

class DiceGame:
    def __init__(self):
        self.players = ["Player X", "Player Y"]
        self.current_player = 0 
        self.playerx = 0
        self.playery = 0

    # Increment player [x, y]
    def player_score(self, player, score):
        if player == self.players[0]:
            self.playerx += score
            return self.playerx
        else:
            self.playery += score
            return self.playery

    # How to repeat the roll when player found number 6
    def rolling_the_dice(self):
        dice_number = random.randint(1,6)
        print(f"\n The dice number {dice_number}")
        total = self.player_score(self.players[self.current_player], dice_number)
        print(f"\n📊 The score of {self.players[self.current_player]} =", total)
        if dice_number == 6 :
            print(f"{self.players[self.current_player]} found {dice_number}. Play again !!!")
        else:
            self.current_player = 1 - self.current_player
   

    # Start the game and handle user input 
    def start(self):
        while True:
            user_input = input(f"\n🎲 {self.players[self.current_player]} Do you want roll the dice ? (Yes/No): ").strip().lower()
            if user_input == "yes" or user_input == "y":
                self.rolling_the_dice()
        
            elif user_input == "no" or user_input =="n":
                return False

            else:
                print("Invalid Input !!!")



pemain = DiceGame()
pemain.start()



    