# Fantasy Football Assistant
With the use of statistics obtain the draft value of list of players. The code
will give you at least 100 players, this can be modified so it can give you a
smallest list.

## How the calculation works:
The formula is:
Player value = (FPTS/G×0.45)+(FPTS×0.30)+((100−AVG)×0.25)

* FPTS/G (45%) → Prioritizes weekly performance (consistency and efficiency per game).
* FPTS (30%) → Rewards total season production.
* 100 - AVG (25%) → Rewards draft value (lower ADP means higher relative value).

## How to use the app:
```
python main.py -a get_stats -p K

Result:
     Player      Team  POS     AVG    FPTS  FPTS/G  DraftValue
  Brandon Aubrey  DAL  K1    88.08   192.0    11.3     65.6650
  Cameron Dicker  LAC  K3   111.08   179.0    10.5     55.6550
   Chris Boswell  PIT  K5   135.42   191.0    11.2     53.4850
      Jake Bates  DET  K2   109.00   161.0     9.5     50.3250
Chase McLaughlin   TB  K4   123.17   164.0     9.6     47.7275
```
Where:
main.py → Script name

-a or --action:
Defines what operation the script should perform.
You can use "add_player" to add a player to a team in Redis, or "get_stats" to retrieve player statistics or rankings.

-n or --name_player:
Specifies the name of the player you want to act on.
This is mainly used with the "add_player" action to identify which player should be added to your team or your rivals’ team.

-p or --position:
Indicates the position you want to analyze.
Valid values include QB, RB, WR, K, TE, or DT.
This option is typically used with "get_stats" to filter data by position.

-t or --team:
Defines which team the selected action applies to.
Use "my_team" to add a player to your fantasy roster, or "rivals_teams" to add them to an opponent’s roster.
