library(nbastatR)

Sys.setenv("VROOM_CONNECTION_SIZE"=131072*10)

assign_nba_players()

players_careers(players = c('LeBron James'))
