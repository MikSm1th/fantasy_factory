library(tidyverse)
library(ggrepel)
library(ggimage)
library(nflfastR)

options(scipen=9999)

data <- load_pbp(2019)
str(data[1:10])

names(data)
View(data)

data %>% select(home_team, away_team, posteam, desc) %>% 
  View()

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
