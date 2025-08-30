from src.read_file import Read_File
import pandas as pd

class Calculations:
    def merge_ftps_and_adp(position:str):
        """"
        Given the data frame and the position it return the ADP, FTPS and FTPS/G for each player.
        """
        adp_data_frame = Read_File.read_adp_csv_file(position=position)
        players_fpts = Read_File.read_positon_csv_file(position=position)
        merged_stats = pd.merge(adp_data_frame, players_fpts, left_on=["Player", "Team"], right_on=["Name", "Team"], how="inner")
        merged_stats["AVG"] = ((merged_stats["AVG"] * 10) / 12).round(2)
        merged_stats = merged_stats.drop(columns=["Name"])
        return merged_stats
    
    def calculate_value_of_player(stats:pd.DataFrame):
        """
        Given a data frame it calculates the value of the player.
        """
        stats["DraftValue"] = (stats["FPTS/G"] * 0.45) + (stats["FPTS"] * 0.3) + (100 - stats["AVG"]) * 0.25
        stats = stats.sort_values(by="DraftValue", ascending=False)
        return stats