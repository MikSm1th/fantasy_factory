library(tidyselect)
library(ggrepel)
library(ggimage)
library(nflfastR)

options(scipen = 9999)

data <- load_pbp(2021)
str(data[1:10])