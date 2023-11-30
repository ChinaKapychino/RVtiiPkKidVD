install.packages(c("rvest", "ggplot2", "dplyr"))

library(rvest)
library(ggplot2)
library(dplyr)

url <- "https://wttr.in/Astana?format=%n+%t+%p"

weather_html <- read_html(url)

weather_text <- html_text(weather_html)

weather_lines <- strsplit(weather_text, "\n")[[1]]

weather_data <- data.frame(
  Дата = as.Date(weather_lines),
  Осадки = as.numeric(sub(" .*", "", weather_lines))
)

# Построение графика
ggplot(weather_data, aes(x = Дата, y = Осадки)) +
  geom_bar(stat = "identity", fill = "blue", alpha = 0.7) +
  labs(title = "График осадков в Астане",
       x = "Дата",
       y = "Осадки (мм)") +
  theme_minimal()
