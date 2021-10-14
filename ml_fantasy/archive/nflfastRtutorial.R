library(tidyverse)
library(ggrepel)
library(ggimage)
library(nflfastR)

options(scipen=9999)

data <- load_pbp(2019)
str(data[1:10])

names(data)
glimpse(data)

data %>% select(home_team, away_team, posteam, desc) %>% 
  glimpse()

data %>% filter(rush ==1 | pass == 1) %>% 
  select(posteam, desc, rush, pass, name, passer, rusher, receiver) %>% 
  head()

data %>% 
  filter(special == 1) %>% 
  select(down, ydstogo, desc) %>% 
  head()

data %>% 
  filter(down == 4) %>% 
  select(down, ydstogo, desc) %>% 
  head()

data %>% 
  filter(down == 4 & special == 0) %>% 
  select(down, ydstogo, desc) %>% 
  head()

pbp_rp <- data %>% 
  filter(rush == 1 | pass == 1, !is.na(epa))

pbp_rp %>% 
  filter(posteam == "DAL", down <= 4, play_type == 'run') %>% 
  group_by(rusher) %>% 
  summarize(
    mean_epa = mean(epa), success_rate = mean(success), 
    ypc = mean(yards_gained), plays = n()
  ) %>% 
  arrange(-mean_epa) %>% 
  filter(plays > 20)

pbp_rp %>% 
  mutate(
    home = if_else(posteam == home_team, 1, 0)
  ) %>% 
  select(posteam, home_team, home) %>% 
  head(10)

pbp_rp %>% 
  mutate(
    home = if_else(posteam == home_team, 1, 0)
  ) %>% 
  group_by(home) %>% 
  summarize(epa = mean(epa))

pbp_rp %>%
  filter(!is.na(cp)) %>%
  mutate(
    depth = case_when(
      air_yards < 0 ~ "Negative",
      air_yards >= 0 & air_yards < 10 ~ "Short",
      air_yards >= 10 & air_yards < 20 ~ "Medium",
      air_yards >= 20 ~ "Deep"
    )
  ) %>%
  group_by(depth) %>%
  summarize(cp = mean(cp))

schotty <- pbp_rp %>%
  filter(wp > .20 & wp < .80 & down <= 2 & qtr <= 2 & half_seconds_remaining > 120) %>%
  group_by(posteam) %>%
  summarize(mean_pass = mean(pass), plays = n()) %>%
  arrange(-mean_pass)
schotty

ggplot(schotty, aes(x = reorder(posteam, -mean_pass), y=mean_pass))+
  geom_text(aes(label=posteam))

pbp <- load_pbp(2020)
glimpse(pbp)

pbp %>% 
  group_by(season) %>% 
  summarize(n = n())

pbp %>% 
  group_by(play_type) %>% 
  summarize(n = n())

qbs <- pbp %>% 
  filter(season_type == "REG", !is.na(epa)) %>% 
  group_by(id, name) %>% 
  summarize(
    epa = mean(qb_epa),
    cpoe = mean(cpoe, na.rm = T),
    n_dropbacks = sum(pass), 
    n_plays = n(),
    team = last(posteam),
  ) %>% 
  ungroup() %>% 
  filter(n_dropbacks > 100 & n_plays > 1000)

head(teams_colors_logos)

qbs <- qbs %>% 
  left_join(teams_colors_logos, by = c('team' = 'team_abbr'))

qbs %>% 
  ggplot(aes(x = cpoe, y = epa)) +
  geom_hline(yintercept = mean(qbs$epa), 
             color = "red", linetype = "dashed", alpha = 0.5)+
  geom_vline(xintercept = mean(qbs$epa), 
             color = "red", linetype = "dashed", alpha = 0.5)+
  geom_point(color = qbs$team_color, 
             cex=qbs$n_plays / 350, alpha = 0.6)+
  geom_text_repel(aes(label=name))+
  stat_smooth(geom='line', alpha=0.5, se=FALSE, method='lm')+
  labs(x="Completion % above expected (CPOE)",
       y="EPA per play(passes, rushes, and penalties)",
       title ="Quarterback Efficiency, 2020",
       caption = "Data: @nflfastR")+
  theme_bw()+
  theme(
    plot.title = element_text(size = 14, hjust = 0.5, face = "bold")
    )+
  scale_y_continuous(breaks = scales::pretty_breaks(n=10))+
  scale_x_continuous(breaks = scales::pretty_breaks(n=10))
  
