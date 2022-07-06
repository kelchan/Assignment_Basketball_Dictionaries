from webbrowser import get


players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]
# Challenge 1: Update the constructor to accept a dictionary (player) as an argument and set the attributes using the dictionary
class Player:
    def __init__( self, player ):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

    @classmethod
    def get_team(cls, team_list): 
        new_team = []
        for player in team_list:
            new_team.append(Player(player))
        print( new_team )


# for player in players:
#     player = Player(player)
#     # print( player.name )

kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}
    

# Complete challenge 2: Create 3 instances of the Player class using the given dictionaries
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)


# Complete challenge 3: Populate a new list with Player instances from the list of players.
# new_team = []
# for player in players:
#     new_team.append(player)
# print(new_team)


# NINJA BONUS :  Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects.
Player.get_team( players )


