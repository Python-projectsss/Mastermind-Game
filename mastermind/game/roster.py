import random

class Roster:
    """A collection of players. The responsibility of Roster is to keep track of the players.
    
    Stereotype: 
        Information Holder

    Attributes:
        _current (integer): The index of the current player.
        _players (list): A list of Player objects.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Roster): an instance of Roster.
        """
        self.current = 0
        self.players = []

        self.process1 = '----'
        self.process2 = '----'
        self.hint1 = []
        self.hint2 = []
        self.random1 = 0
        self.random2 = 0
        self.empty = '****'
        self.game_over = False
        
    def add_player(self, player):
        """Adds the given player to the roster
        
        Args:
            self (Roster): An instance of Roster.
            player (Player): The player object to add.
        """
        if player not in self.players:
            self.players.append(player)

    def get_current(self):
        """Gets the current player object.
        
        Args:
            self (Roster): An instance of Roster.
        
        Returns:
            Player: The current player.
        """
        return self.players[self.current]

    def get_process(self):
        """
        Will return the process 
        """

        if self.current == 0:
            return self.process1
        if self.current ==1:
            return self.process2

    def get_hint(self):
        """
        Will return the process 
        """

        if self.current == 0:
            return self.hint1
        if self.current ==1:
            return self.hint2


    
    def next_player(self):
        """Advances the turn to the next player.
        
        Args:
            self (Roster): An instance of Roster.
        """
        self.current = (self.current + 1) % len(self.players)

    def player1(self):
        """
        Display the player 1 name 
        """

        return self.players[0]

    def player2(self):

        return self.players[1]


    def set_process(self, number):
        """
        Will set the process of the user
        """


        if self.current == 0:
            self.process1= number
            
        if self.current ==1:
            self.process2= number


    def process1_return(self):

        return self.process1

    def process2_return(self):

        return self.process2

    def hint1_return(self):

        if len(self.hint1) == 0:
            return self.empty
        else: 
            hint1 = ' '.join([str(elem) for elem in self.hint1])
            return hint1

    def hint2_return(self):

        if len(self.hint2) == 0:
            return self.empty
        else:
            hint2 = ' '.join([str(elem) for elem in self.hint2])
            return hint2

    def hint(self, user):
        """

        """

        list_user = list(map(int, str(user)))
        list_random1 = list(map(int, str(self.random1)))
        list_random2 = list(map(int, str(self.random2)))

        if self.current == 0:

            self.hint1.clear()

            if list_user == list_random1:
                self.game_over = True

            counter = 0

            for a in list_user:
                if a in list_random1:
                    if a == list_random1[counter]:
                        self.hint1.append('x')
                    else:
                        self.hint1.append('o')
                else:
                    self.hint1.append('*')

                counter +=1
                    

        if self.current == 1:

            self.hint2.clear()
            if list_user == list_random2:
                self.game_over = True
            counter = 0
            for a in list_user:
                if a in list_random2:
                    
                    if a == list_random2[counter]:
                        self.hint2.append('x')
                    else:
                        self.hint2.append('o')
                else:
                    self.hint2.append('*')

                counter +=1
                    


    def win(self):
        """
        It will compare the numbers if they are the same the user won the game
        """
        return self.game_over

    def random_numbers(self):

        self.random1 = random.randint(1000, 9999)

        print("The random number for 1 is ", self.random1)
        self.random2 = random.randint(1000, 9999)

        print("The random number for 2 is ", self.random2)



