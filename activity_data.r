people <- c("Бекжан", "Максим", "Вали", "Чингис", "Дима", "Нурасыл", "Кизатов", "Артур")

digits <- c(6, 6, 4, 4, 4, 3, 3, 2)

data <- data.frame(people, digits)

data <- data[order(data$digits, decreasing = TRUE),]

barplot(data$digits, names.arg = data$people, col = "skyblue", main = "Количество пропусков занятий", xlab = "Количество занятий", ylab = "Люди", beside = TRUE)
