import os
import random

class Ocean:

    """Creates 2D array the represents an ocean grid
    to veiw your ship positions

    Class contains all functions needed for placing
    ships on the ocean grid"""

    def __init__(self, width=10, height=10):
        self.ocean = [["~" for i in range(width)] for i in range(height)]

    def __getitem__(self, point):
        row, col = point
        return self.ocean[row][col]

    def __setitem__(self, point, value):
        row, col = point
        self.ocean[row][col] = value

    def view_ocean(self):
        for row in self.ocean:
            print(" ".join(row))

    # Two functions check a coordinate input is on the grid

    def valid_col(self, row):
        try:
            self.ocean[row]
            return True
        except IndexError:
            return False

    def valid_row(self, col):
        try:
            self.ocean[0][col]
            return True
        except IndexError:
            return False

    # Two functions check for valid board space for ship placement

    def can_use_col(self, row, col, size):

        valid_coords = []

        for i in range(size):

            if self.valid_col(col) and self.valid_row(row):
                if self.ocean[row][col] == "~":
                    valid_coords.append((row, col))
                    col = col + 1
                else:
                    col = col + 1
            else:
                return False

        if size == len(valid_coords):
            return True
        else:
            return False

    def can_use_row(self, row, col, size):

        valid_coords = []

        for i in range(size):

            if self.valid_row(row) and self.valid_col(col):
                if self.ocean[row][col] == "~":
                    valid_coords.append((row, col))
                    row = row + 1
                else:
                    row = row + 1
            else:
                return False

        if size == len(valid_coords):
            return True
        else:
            return False

    # Corresponding fucntions set ship counters on valid space

    def set_ship_col(self, row, col, size):
        for i in range(size):
            self.ocean[row][col] = "S"
            col = col + 1

    def set_ship_row(self, row, col, size):
        for i in range(size):
            self.ocean[row][col] = "S"
            row = row + 1

class Radar:

    """Creates a grid to track the state of an opponent's ocean grid"""

    def __init__(self, width=10, height=10):
        self.radar = [["." for i in range(width)] for i in range(height)]

    def __getitem__(self, point):
        row, col = point
        return self.radar[row][col]

    def __setitem__(self, point, value):
        row, col = point
        self.radar[row][col] = value

    def view_radar(self):
        for row in self.radar:
            print(" ".join(row))

class Ship:

    def __init__(self, ship_type, size):
        self.ship_type = ship_type
        self.size = size
        self.coords = []

    def plot_vertical(self, row, col):
        for i in range(self.size):
            self.coords.append((row, col))
            row = row + 1

    def plot_horizontal(self, row, col):
        for i in range(self.size):
            self.coords.append((row, col))
            col = col + 1

    def check_status(self):
        if self.coords == []:
            return True
        else:
            return False

class Player:

    ships = {"Aircraft Carrier": 5, "Crusier": 4, "Destroyer": 3, 
"Submarine": 2}

    def __init__(self, name):
        self.ocean = Ocean()
        self.radar = Radar()
        self.name = name
        self.fleet = []

   # Function uses player input to set up fleet positions on a player board.
   # For each ship, a ship object containing relevant coordinates is appended to self.fleet

    def set_fleet(self):
        input("Pick a coordinate between 0 and 9 for the columns and rows on your board")
        input("Boats are placed form right to left.")
        for ship, size in self.ships.items():

            flag = True
            while flag:
                self.view_console()
                try:
                    print("Place your %s" % (ship))
                    row = int(input("Pick a row -----> "))
                    col = int(input("Pick a column -----> "))
                    orientation = str(input("Vertical or Horizontal? (choose v or h) -----> "))

                    if orientation in ["v", "V"]:
                        if self.ocean.can_use_row(row, col, size):
                            self.ocean.set_ship_row(row, col, size)
                            boat = Ship(ship, size)
                            boat.plot_vertical(row, col)
                            self.fleet.append(boat)
                            flag = False
                        else:
                            input("Overlapping ships, try again")

                    elif orientation in ["h", "H"]:
                        if self.ocean.can_use_col(row, col, size):
                            self.ocean.set_ship_col(row, col, size)
                            boat = Ship(ship, size)
                            boat.plot_horizontal(row, col)
                            self.fleet.append(boat)
                            flag = False
                        else:
                            input("Overlapping ships, try agin")

                    else:
                        continue

                    self.view_console()
                    input()
                    os.system('clear')

                except ValueError:
                    print("Don't you remember your training?\nType a number..\n")

    # Function displays player ocean/radar in readable format

    def view_console(self):
        self.radar.view_radar()
        print("|                 |")
        self.ocean.view_ocean()

    # Function checks status of ship objects within player fleet

    def register_hit(self, row, col):
        for boat in self.fleet:
            if (row, col) in boat.coords:
                boat.coords.remove((row, col))
                if boat.check_status():
                    self.fleet.remove(boat)
                    print("%s's %s has been sunk!" % (self.name, boat.ship_type))

    # Player interface for initiating in-game strikes,
    # updates the state of the boards of both players

    def strike(self, target):
        self.view_console()
        try:
            print("\n%s Pick your target..." % (self.name))
            row = int(input("Pick a row -----> "))
            col = int(input("Pick a column -----> "))

            if self.ocean.valid_row(row) and self.ocean.valid_col(col):
                if target.ocean.ocean[row][col] == "S":
                    print("DIRECT HIT!!!")
                    target.ocean.ocean[row][col] = "X"
                    target.register_hit(row, col)
                    self.radar.radar[row][col] = "X"

                else:
                    if self.radar.radar[row][col] == "O":
                        print("Area already hit....Check your radar!")
                        self.strike(target)
                    else:
                        print("Negative...")
                        self.radar.radar[row][col] = "O"

            else:
                print("Coordinates out of range...")
                self.strike(target)

        except ValueError:
            print("You need to provide a number....\n")
            self.strike(target)
        input()
        os.system('clear')

class Computer(Player):

    def __init__(self):
        super().__init__(self)
        self.name = "Computer"

    # Automated version of set_fleet function from Player

    def set_compu_fleet(self):
        positions = ["v", "h"]

        for ship, size in self.ships.items():

            flag = True
            while flag:
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                orientation = random.choice(positions)

                if orientation == "v":
                    if self.ocean.can_use_row(row, col, size):
                        self.ocean.set_ship_row(row, col, size)
                        boat = Ship(ship, size)
                        boat.plot_vertical(row, col)
                        self.fleet.append(boat)
                        flag = False

                    else:
                        row = row + 2

                elif orientation == "h":
                    if self.ocean.can_use_col(row, col, size):
                        self.ocean.set_ship_col(row, col, size)
                        boat = Ship(ship, size)
                        boat.plot_horizontal(row, col)
                        self.fleet.append(boat)
                        flag = False

                    else:
                        col = col + 2

                else:
                    continue

    # Automated strike function

    def compu_strike(self, target):
        row = random.randint(0, 9)
        col = random.randint(0, 9)

        if self.radar.radar[row][col] == ".":
            input("...Target acquired....%s, %s" % (row, col))

            if target.ocean.ocean[row][col] == "S":
                print("DIRECT HIT!")
                target.ocean.ocean[row][col] = "X"
                target.register_hit(row, col)
                self.radar.radar[row][col] = "X"

            else:
                print("Missed....recalibrating")
                self.radar.radar[row][col] = "O"

        else:
            self.compu_strike(target)

class BattleshipsPVP:
    """creates a game of battlehsips"""

    def __init__(self):
        start = input("Begin? (y or n) -----> ")
        if start in ["y", "Y"]:
            self.playPVP()
        else:
            print("Aborted...")

    def playPVP(self):
        p1name = input("Player 1, state your name! -----> ")
        p1 = Player(p1name)
        p1.set_fleet()
        p1.view_console()
        self.clear_screen()

        p2name = input("\n\nPlayer 2, state your name! -----> ") 
        p2 = Player(p2name)
        p2.set_fleet()
        p2.view_console()
        self.clear_screen()

        flag = True
        while flag is True:
            p1.strike(p2)
            if self.fleet_sunk(p2) is True:
                self.victory_message(p1, p2)
                flag = False
            else:
                self.clear_screen()

                p2.strike(p1)
                if self.fleet_sunk(p1) is True:
                    self.victory_message(p2, p1)
                    flag = False
                else:
                    self.clear_screen()
        print("\nThanks for playing!")

    # Function checks remaining ship counters on a player's board

    def fleet_sunk(self, player):
        ship_counters = 0
        """Traverses grid looking for 's' counters"""
        for row in range(len(player.ocean.ocean)):
            for col in range(len(player.ocean.ocean)):
                if player.ocean.ocean[row][col] == "S":
                    ship_counters += 1
        if ship_counters == 0:
            return True
        else:
            return False

    def clear_screen(self):
        input("\nNext Turn?")
        os.system('clear')

    def victory_message(self, winner, loser):
        print("\n\n\n*****************************************")
        print("%s's fleet has been destroyed, %s wins!" % (loser.name, winner.name))
        print("*****************************************")

class BattleshipsCOMP(BattleshipsPVP):

    def __init__(self):
        start = input("Begin? (y or n) -----> ")
        if start in ["y", "Y"]:
            self.playCOMP()
        else:
            print("Aborted...")

    def playCOMP(self):
        pname = input("Player 1, state your name! -----> ")
        p = Player(pname)
        p.set_fleet()
        p.view_console()
        self.clear_screen()

        c = Computer()
        print("Computer setting its fleet...")
        c.set_compu_fleet()
        self.clear_screen()

        flag = True
        while flag is True:
            p.strike(c)
            if self.fleet_sunk(c) is True:
                self.victory_message(p, c)
                flag = False
            else:
                self.clear_screen()

                c.compu_strike(p)
                if self.fleet_sunk(p) is True:
                    self.victory_message(c, p)
                    flag = False
                else:
                    self.clear_screen()
        print("\nThanks for playing!")

# Script initiates game of battleships


def playbattleships():
    print("\n\n***********************")
    print("Welcome to Battleships!")
    print("***********************\n")

    print("\n 1) Player vs Player")
    print("\n 2) Player vs Computer")

    flag = True

    while flag:
        try:
            mode = int(input("\n\nPick a number to select a game mode ----> "))
            if mode == 1:
                flag = False
                BattleshipsPVP()
            elif mode == 2:
                flag = False
                BattleshipsCOMP()
            else:
                continue
        except ValueError:
            print("You can only pick either option 1 or 2")


playbattleships()