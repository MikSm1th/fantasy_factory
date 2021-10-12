library(nflfastR)

wkly_plyr_stats <- function(yr){
  get_pbp <- load_pbp(yr)
  wkly_plyr_stats <- calculate_player_stats(get_pbp, weekly=TRUE)
  write.csv(plyr_stats_2020, paste('data/wkly_plyr_stats_',yr,'.csv'))
}

wkly_plyr_stats(2020)



