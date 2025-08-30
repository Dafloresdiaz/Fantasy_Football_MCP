from optparse import OptionParser
from src.calculations import Calculations
from src.db_operations import DBOperations

if __name__ == "__main__":
    db_operations = DBOperations()
    parser = OptionParser()
    parser.add_option("-a", "--action", type =str, dest="action", 
                      help="Action to perform: 'add_player' or 'get_stats'")
    parser.add_option("-n", "--name_player", type=str, dest="name_player", 
                      help="Add a player to your team or rivals team")
    parser.add_option("-p", "--position", type=str, dest="position", 
                      help="Position to analyze: QB, RB, WR, K, TE or DT")
    parser.add_option("-t", "--team", type=str, dest="team", 
                      help="Specify if the player is for 'my_team' or 'rivals_teams'")

    
    parameters, _ = parser.parse_args()


    if parameters.action == "add_player":
        # Add a player to the respective team
        if parameters.position and parameters.name_player and parameters.team:
            if parameters.team == "my_team":
                if db_operations.get_player_from_team(parameters.team, parameters.name_player):
                    print(f"The player {parameters.name_player} is already in your team")
                else:
                    db_operations.add_player_to_team(
                        team=parameters.team,
                        player_name=parameters.name_player,
                        position=parameters.position
                    )
            elif parameters.team == "rivals_teams":
                if db_operations.get_player_from_team(parameters.team, parameters.name_player):
                    print(f"The player {parameters.name_player} is already in your rivals team")
                else:
                    db_operations.add_player_to_team(
                        team=parameters.team,
                        player_name=parameters.name_player,
                        position=parameters.position
                    )
            else:
                raise ValueError("Team not recognized, please provide 'my_team' or 'rivals_teams'")
    
    elif parameters.action == "get_stats":
        # Get the stats for a position and calculate the value of the player
        if parameters.position:
            adp_by_positiion = Calculations.merge_ftps_and_adp(
                parameters.position
            )
            valued_players = Calculations.calculate_value_of_player(
                stats=adp_by_positiion
            )
            print(valued_players.head(50).to_string(index=False))

    elif parameters.action == "get_players":
        if parameters.team:
            print(db_operations.get_players_from_team(team=parameters.team))

    elif parameters.action == "remove_player":
        if parameters.team and parameters.name_player:
            db_operations.remove_player_from_team(
                team=parameters.team,
                player_name=parameters.name_player
            )