import json
import pandas as pd

class CricketPlayer:
    def _init_(self, name, role, batting_average, bowling_average, strike_rate):
        self.name = name
        self.role = role
        self.batting_average = batting_average
        self.bowling_average = bowling_average
        self.strike_rate = strike_rate

class IPLTeam:
    def _init_(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                print(f"{player_name} removed from {self.name}")
                return
        print(f"{player_name} not found in {self.name}")

    def to_dict(self):
        return {
            "name": self.name,
            "players": [player._dict_ for player in self.players]
        }

    @staticmethod
    def from_dict(data):
        team = IPLTeam(data["name"])
        team.players = [CricketPlayer(**player_data) for player_data in data["players"]]
        return team

class IPLRosterManager:
    def _init_(self):
        self.teams = {}
        self.players = []

    def load_data(self):
        try:
            with open("players.json", "r") as player_file:
                self.players = [CricketPlayer(**player_data) for player_data in json.load(player_file)]
        except FileNotFoundError:
            pass
        
        try:
            with open("teams.json", "r") as team_file:
                teams_data = json.load(team_file)
                self.teams = {team_name: IPLTeam.from_dict(team_data) for team_name, team_data in teams_data.items()}
        except FileNotFoundError:
            pass

    def save_data(self):
        with open("teams.json", "w") as team_file:
            json.dump({team_name: team.to_dict() for team_name, team in self.teams.items()}, team_file)

        with open("players.json", "w") as player_file:
            json.dump([player._dict_ for player in self.players], player_file)

    def create_team(self, team_name):
        if team_name not in self.teams:
            self.teams[team_name] = IPLTeam(team_name)
            print(f"IPL Team '{team_name}' created.")
        else:
            print(f"IPL Team '{team_name}' already exists.")

    def add_player_to_pool(self, player):
        self.players.append(player)
        self.save_data()
        print(f"{player.name} added to the player pool.")

    def remove_player_from_pool(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                self.save_data()
                print(f"{player_name} removed from the player pool.")
                return
        print(f"{player_name} not found in the player pool.")

    def create_balanced_teams(self, num_teams):
        sorted_players = sorted(self.players, key=lambda player: player.batting_average if player.role == "Batsman" else player.bowling_average if player.role == "Bowler" else 0, reverse=True)
        teams = [[] for _ in range(num_teams)]
        for i, player in enumerate(sorted_players):
            teams[i % num_teams].append(player)
        return teams

    def display_team_rosters(self):
        for team_name, team in self.teams.items():
            team_df = self.team_to_dataframe(team)
            print(f"\nTeam Roster for {team_name}:")
            print(team_df)
            print()

    def update_teams(self):
        num_teams = len(self.teams)
        teams = self.create_balanced_teams(num_teams)
        for i, team_name in enumerate(self.teams.keys()):
            self.teams[team_name].players = teams[i]

    def remove_player_from_team(self, team_name, player_name):
        if team_name in self.teams:
            self.teams[team_name].remove_player(player_name)
            self.remove_player_from_pool(player_name)  # Remove player from pool as well
            self.update_teams()
        else:
            print(f"IPL Team '{team_name}' not found.")
    
    def players_to_dataframe(self):
        player_data = []
        for player in self.players:
            player_data.append([player.name, player.role, player.batting_average, player.bowling_average, player.strike_rate])
        return pd.DataFrame(player_data, columns=["Name", "Role", "Batting Average", "Bowling Average", "Strike Rate"])

    def team_to_dataframe(self, team):
        team_data = []
        for player in team.players:
            team_data.append([team.name, player.name, player.role, player.batting_average, player.bowling_average, player.strike_rate])
        return pd.DataFrame(team_data, columns=["Team", "Player Name", "Role", "Batting Average", "Bowling Average", "Strike Rate"])

# Function to create a player
def create_player():
    name = input("Enter player's name: ")
    role = input("Enter player's role (Batsman/Bowler/All-rounder): ").lower()
    
    if role not in ['batsman', 'bowler', 'all-rounder']:
        print("Invalid role entered.")
        return None
    
    batting_average = None
    bowling_average = None
    
    if role == "batsman":
        batting_average = float(input("Enter player's batting average: "))
    elif role == "bowler":
        bowling_average = float(input("Enter player's bowling average: "))
    else:  # For all-rounders
        batting_average = float(input("Enter player's batting average: "))
        bowling_average = float(input("Enter player's bowling average: "))
    
    strike_rate = float(input("Enter player's strike rate: "))
    return CricketPlayer(name, role, batting_average, bowling_average, strike_rate)

# Modify the example usage part:

roster_manager = IPLRosterManager()
roster_manager.load_data()

# Function to handle adding initial players to the pool
def add_initial_players():
    num_players = int(input("Enter the number of initial players to add: "))
    for _ in range(num_players):
        player = create_player()
        if player:
            roster_manager.add_player_to_pool(player)
    assign_players_to_teams()

# Function to handle adding new players to the pool
def add_new_players():
    num_players = int(input("Enter the number of new players to add: "))
    for _ in range(num_players):
        player = create_player()
        if player:
            roster_manager.add_player_to_pool(player)
    roster_manager.update_teams()
    roster_manager.display_team_rosters()

# Function to assign players to teams
def assign_players_to_teams():
    num_teams = int(input("Enter the number of teams: "))
    for i in range(num_teams):
        team_name = input(f"Enter name for Team {i+1}: ")
        roster_manager.create_team(team_name)
    roster_manager.update_teams()
    roster_manager.display_team_rosters()

# Function to remove a player from a team
def remove_player_from_team():
    team_name = input("Enter the name of the team: ")
    player_name = input("Enter the name of the player to remove: ")
    roster_manager.remove_player_from_team(team_name, player_name)

# Example usage:
add_initial_players()

while True:
    print("\nMenu:")
    print("1. Add new players")
    print("2. Remove player from a team")
    print("3. View team rosters")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_new_players()
    elif choice == "2":
        remove_player_from_team()
    elif choice == "3":
        roster_manager.display_team_rosters()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")