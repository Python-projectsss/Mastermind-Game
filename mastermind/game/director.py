from game.console import Console
from game.move import Move
from game.player import Player
from game.roster import Roster

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        board (Hunter): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        move (Rabbit): An instance of the class of objects known as Move.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._console = Console()
        self._keep_playing = True
        self._move = None
        self._roster = Roster()

        self.secret_number_1 = 0
        self.secret_number_2 = 0 
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)

        self._roster.random_numbers()

        
    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        # display the game board
        print("--------------------")

        player1 = self._roster.player1()
        player2 = self._roster.player2()
        self._console.write(f" Player {player1.get_name()}: {self._roster.process1_return()}, {self._roster.hint1_return()}")
        self._console.write(f" Player {player2.get_name()}: {self._roster.process2_return()}, {self._roster.hint2_return()}")
        print("--------------------")
        
        # get next player's move
        player = self._roster.get_current()
        self._console.write(f" {player.get_name()}'s turn: ")
        number = self._console.read_number("What is your guess? ")
        self._roster.set_process(number)
        self._roster.hint(number)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
        if self._roster.win() == True:
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n Amazing {name} won! \n Congreatulations !!!!")
            self._keep_playing = False
        self._roster.next_player()

    