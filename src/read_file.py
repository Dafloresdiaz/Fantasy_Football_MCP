# Read files for the position QB, RB, WR, K, TE
import pandas as pd

class Read_File:
    def read_adp_csv_file(position:str):
        """
        Read the CSV file using pandas to return a data frame.
        """
        data_frame = pd.read_csv("csv_files/adp_rank_ppr.csv")
        filter_adp = data_frame[data_frame['POS'].str.startswith(position)].sort_values("AVG")
        filter_adp = filter_adp[["Player", "Team", "POS", "AVG"]]
        return filter_adp
    
    def read_positon_csv_file(position:str):
        """
        Depending on the position given reads the corresponding CSV file. 
        """
        data_frame = None
        if position == "QB":
            data_frame = pd.read_csv("csv_files/quarterback_stats_v2.csv")
        elif position == "RB":
            data_frame = pd.read_csv("csv_files/running_back_stats_v2.csv")
        elif position == "WR":
            data_frame = pd.read_csv("csv_files/wide_reciever_stats_v2.csv")
        elif position == "TE":
            data_frame = pd.read_csv("csv_files/tail_back_stats_v2.csv")
        elif position == "DT":
            data_frame = pd.read_csv("csv_files/defense_stats.csv")
        elif position == "K":
            data_frame = pd.read_csv("csv_files/kicker_stats.csv")
        else:
            raise ValueError("Position not recognized, please provide a valid position")
        
        filter_fpts = data_frame[["Player", "FPTS", "FPTS/G"]].copy()
        filter_fpts["Name"] = filter_fpts["Player"].str.split("(").str[0].str.strip()
        filter_fpts["Team"] = filter_fpts["Player"].str.split("(").str[1].str.replace(")","").str.strip()
        filter_fpts = filter_fpts[["Name", "Team", "FPTS", "FPTS/G"]]
        filter_fpts = filter_fpts[filter_fpts["Team"] != "FA"]
        return filter_fpts