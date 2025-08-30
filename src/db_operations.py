import redis

class DBOperations:

    def __init__(self):
        self.redis_client = redis.Redis(
            host='localhost', 
            port=6379, 
            db=0, 
            decode_responses=True
        )
    
    def add_player_to_team(self,team:str, player_name:str, position:str):
        self.redis_client.hset(
            team, mapping={
                player_name: position
            }
        )
    
    def get_player_from_team(self, team:str, player_name:str):
        return self.redis_client.hexists(team, player_name)
    
    def get_players_from_team(self, team:str):
        return self.redis_client.hgetall(team)
    
    def remove_player_from_team(self, team:str, player_name:str):
        self.redis_client.hdel(team, player_name)
        print(f"The player {player_name} has been removed from {team}")
