library(tidyverse)
library(quantmod)
library(TTR)

# Load data
spy_data <- read.csv("../data/spy_data.csv")

# Compute moving averages
spy_data$SMA10 <- SMA(spy_data$Close, n=10)
spy_data$SMA50 <- SMA(spy_data$Close, n=50)

# Simple predictive signal: 1 = buy, -1 = sell
spy_data$Signal <- ifelse(spy_data$SMA10 > spy_data$SMA50, 1, -1)

# Save results
write.csv(spy_data, "../data/spy_signals_r.csv", row.names=FALSE)
