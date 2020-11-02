class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def first_game(self, player1, player2):
        lets_play(player1, player2)
        if player1.choice == choice1 and player2.choice == choice2:
            return "rock beats scissors - player 1 wins"
    
    # def game(self, player1, player2):
    #     choice1 = Choice1("rock")
    #     choice2 = Choice2("scissors")
    #     choice3 = Choice3("paper")
        # if player1.choice == choice1 and player2.choice == choice2:
        #     return "rock beats scissors - player 1 wins"
        # elif player1(input) == choice2 and player2(input) == choice3:
        #     return "scissors beat paper - player 1 wins"
        # elif player1(input) == choice3 and player 2(input) == choice1:
        #     return "paper beats rock - player 1 wins"
        # elif player1(inout) == choice2 and player2(inout) == choice1:
        #     return "rock beats scissors - player 2 wins"
        # elif player1(input) == choice3 and player2(inout) == choice2:
        #     return "scissors beat paper - player 2 wins"
        # elif player1(input) == choice1 and player2(input) == choice3
        #     return "paper beats rock - player 2 wins"
        # elif player1(input) == choice1 and player2(input) == choice1
        #     return "rock draws with rock - game is tied"
        # elif player1(input) == choice2 and player2(input) == choice2
        #     return "scissors draws with scissors - game is tied"
        # else player1(input) == choice3 and player2(input) == choice3
        #     return "paper draws with paper - game is tied"