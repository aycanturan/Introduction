import random
# !/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = None
    their_move = None

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Enter: rock, paper or scissors >")
            if move in moves:
                return move
            print(f"wrong input")


class ReflectPlayer(Player):
    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move


class CyclePlayer(Player):
    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        index = moves.index(self.my_move) + 1
        return moves[index % len(moves)]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.s1 = 0
        self.s2 = 0

    def play_round(self, round):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2):
            self.s1 += 1
            print(f"You win round {round}")
        elif beats(move2, move1):
            self.s2 += 1
            print(f"Computer wins round {round}")
        else:
            print(f"Nobody wins round {round}")

    def play_game(self):
        print("Rock Paper Scissors by Aycan")
        print(f"YOU aganist computer, start!")

        for round in range(5):
            print(f"Round {round}: SCORE: {self.s1}- {self.s2}")
            self.play_round(round)

        if self.s1 > self.s2:
            print(f"YOU win the GAME - SCORE: {self.s1}-{self.s2}")
        elif self.s2 > self.s1:
            print(f"Computer wins the GAME - SCORE: {self.s2}-{self.s1}")
        else:
            print(f"GAME TIE - SCORE: {self.s1}-{self.s2} ")

        print("Game finished!")


if __name__ == '__main__':
    players = [
        AllRockPlayer(),
        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game()
